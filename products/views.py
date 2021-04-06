from django.shortcuts import render, redirect
from  .models import Product, UserOrder, VisitorOrder, ProductCredit
from .forms import UserOrderForm, VisitorOrderForm, ProductCreditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from users.models import ProductCustomer
import random

def showProduct(request):
	products = Product.objects.all()
	form = UserOrderForm()
	guest_form = VisitorOrderForm()
	if request.method == 'POST':
		form = UserOrderForm(request.POST or None)
		guest_form = VisitorOrderForm(request.POST or None)
		if guest_form.is_valid():
			guest_form.save()
			visitor = VisitorOrder.objects.filter(order_Id=2021)[0]
			visitor.order_Id = "BQ" + str(random.randint(10000000,99999999))
			if visitor.state == "Select a State":
				messages.error(request, "Please select a state from dropdown")
				visitor.delete()
			else:
				visitor.save()
				name = guest_form.cleaned_data.get('name')
				email = guest_form.cleaned_data.get('email')
				# send_mail(
				# 	'Guest Order [' + str(name) + ']',
				# 	'Dear ' + str(name) + ', your order has been received. If you have not paid you can follow this link www.buildqwik.ng/visitor-pay/ to do so',
				# 	'yustaoab@gmail.com',
				# 	[email],
				# 	fail_silently=False
				# )
				messages.success(request, "Your order has been placed! Please make payment below")
				return redirect('guest_pay')
		elif form.is_valid():
			form.save(commit=False).user = request.user
			form.save()
			reg = UserOrder.objects.filter(order_Id=2021)[0]
			reg.order_Id = "BQ" + str(random.randint(10000000,99999999))
			if reg.state == "Select a State":
				reg.state = reg.user.productcustomer.state
			if reg.email == "":
				reg.email = reg.user.email
			if reg.phone_Number == "":
				reg.phone_Number = reg.user.productcustomer.phone_Number
			if reg.city == "":
				reg.city = reg.user.productcustomer.city
			if reg.address == "":
				reg.address = reg.user.productcustomer.address
			reg.save()
			customer = ProductCustomer.objects.get(user=request.user)
			first_name = customer.user.first_name
			last_name = customer.user.last_name
			email = customer.user.email
			# send_mail(
			# 	'Registered User [' + str(first_name) + ' ' + str(last_name) + ']',
			# 	'Dear ' + str(first_name) + ', your order has been received. Remember you can always log in and checkout to pay from your dashboard',
			# 	'yustaoab@gmail.com',
			# 	[email],
			# 	fail_silently=False
			# )
			messages.success(request, "Order submitted! You can checkout below")
			return redirect('orders')
		else:
			messages.error(request, "Please make sure you don't enter too much characters than necessary")
	context = {'products': products, 'form': form, 'guest_form': guest_form}
	return render(request, 'product/store.html', context)

@login_required
def fundWallet(request, **kwargs):
	form = ProductCreditForm()
	if request.method == 'POST':
		form = ProductCreditForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=False).user = request.user
			form.save()
			customer = ProductCustomer.objects.get(user=request.user)
			first_name = customer.user.first_name
			last_name = customer.user.last_name
			email = customer.user.email
			send_mail(
                'Credit Wallet [' + str(first_name) + ' ' + str(last_name) + ']',
                'Dear ' + str(first_name) + ', Your request has been received! Your wallet will be funded as soon as your payment is verified',
                'yustaoab@gmail.com',
				[email],
                fail_silently=False
            )
			messages.success(request, "Request Submitted, Your wallet will be funded as soon as your payment is verified")
			return redirect('dashboard')
		else:
			messages.error(request, "Please make sure you don't enter too much characters than necessary")
	context = {'form': form}
	return render(request, 'product/customercredit_form.html', context)
