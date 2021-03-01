from django.shortcuts import render, redirect
from django.db.models import Count
from .filters import ContactFilter
from  .models import Contact
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

def showHome(request):
    return render(request, 'home/home.html')

def showAbout(request):
    return render(request, 'home/about.html')

@permission_required('home.view_Contact')
def showContacts(request):
    context = {}
    filtered_contacts = ContactFilter(
        request.GET,
        queryset = Contact.objects.all()
    )
    context['filtered_contacts'] = filtered_contacts
    paginated_filtered_contacts = Paginator(filtered_contacts.qs, 10)
    page_number = request.GET.get('page')
    contacts_page_obj = paginated_filtered_contacts.get_page(page_number)
    context['contacts_page_obj'] = contacts_page_obj
    total_contacts = filtered_contacts.qs.count()
    context['total_contacts'] = total_contacts
    return render(request, 'home/contact_list.html', context=context)

def showContact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, str(name) + ", your message will receive attention shortly")
        else:
            return redirect('contact')
    return render(request, 'home/contact_form.html', {'form': form})

    # if request.method == 'POST':
    #     contact = request.POST['contact']
    #     contact_id = request.POST['contact_id']
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     message = request.POST['message']
    #     user_id = request.POST['user_id']
    #     contact = Contact(contact=contact, contact_id=contact_id, name=name, email=email, phone_number=phone_number, message=message, user_id=user_id)
    #     contact.save()
    #     messages.success(request, str(name) + ", your message has been submitted and will receive attention shortly")
    #     return redirect('/contact-us/'+contact_id )
    # return render(request, 'home/contact_form.html')

def showCement(request):
    return render(request, 'home/cement.html')

def showRoofing(request):
    return render(request, 'home/roofing.html')
