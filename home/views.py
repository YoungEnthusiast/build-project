from django.shortcuts import render, redirect
from django.db.models import Count
from .filters import ContactFilter
from  .models import Contact, Advert
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date

def showHome(request):
    adverts = Advert.objects.filter(expiry__gte=date.today())
    context = {'adverts': adverts}
    return render(request, 'home/home.html', context)

def showAbout(request):
    return render(request, 'home/about.html')

@login_required
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
            email = form.cleaned_data.get('email')
            send_mail(
                'Contact BuildQwik',
                'A message was sent by ' + name + '. Please log in to admin panel to read message',
                'admin@buildqwik.ng',
                [email, 'hello@buildqwik.ng'],
                fail_silently=False
            )
            messages.success(request, str(name) + ", your message will receive attention shortly")
        else:
            return redirect('contact')
    return render(request, 'home/contact_form.html', {'form': form})
