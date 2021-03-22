from django.shortcuts import render, redirect
from  .models import Cement, CementOrder, GuestCementOrder
from .forms import CementOrderForm, GuestCementOrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from users.models import Customer

def showCement(request):
	cements = Cement.objects.all()
	form = CementOrderForm()
	guest_form = GuestCementOrderForm()
	if request.method == 'POST':
		form = CementOrderForm(request.POST or None)
		guest_form = GuestCementOrderForm(request.POST or None)
		if guest_form.is_valid():
			guest_form.save()
			name = guest_form.cleaned_data.get('name')
			email = guest_form.cleaned_data.get('email')
			send_mail(
                'Guest Order [' + name + ']',
                name + ', Your order has been received. If you have not paid you can follow this link www.buildqwik.ng/products/cement/guest-pay/ to do so',
                'yustaoab@gmail.com',
				[email],
                fail_silently=False
            )
			messages.success(request, "Your order has been placed! Please make payment below")
			return redirect('guest_pay')

		elif form.is_valid():
			form.save(commit=False).user = request.user
			form.save()
			nam = Customer.objects.get(user=request.user)
			name = nam.user.first_name
			email = nam.user.email
			# name = form.cleaned_data.get('name')
			# email = form.cleaned_data.get('email')
			send_mail(
                'Registered User [' + name + ']',
                name + ', Your order has been received. Remember you can always log in and checkout to pay from your dashboard',
                'yustaoab@gmail.com',
				[email],
                fail_silently=False
            )
			messages.success(request, "Order submitted! You can checkout below")
			return redirect('dashboard')
		else:
			messages.error(request, "ERROR: Please make sure you don't enter too much characters than necessary")
	context = {'cements': cements, 'form': form, 'guest_form': guest_form}
	return render(request, 'cement/store.html', context)
