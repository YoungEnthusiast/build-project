# from django.shortcuts import render, redirect
# from  .models import Product, ProductOrder, GuestProductOrder, CustomerCredit
# from .forms import ProductOrderForm, GuestProductOrderForm, CustomerCreditForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required, permission_required
# from django.core.mail import send_mail
# from users.models import Customer
#
# def showProduct(request):
# 	products = Product.objects.all()
# 	form = ProductOrderForm()
# 	guest_form = GuestProductOrderForm()
# 	if request.method == 'POST':
# 		form = ProductOrderForm(request.POST or None)
# 		guest_form = GuestProductOrderForm(request.POST or None)
# 		if guest_form.is_valid():
# 			guest_form.save()
# 			# name = guest_form.cleaned_data.get('name')
# 			# email = guest_form.cleaned_data.get('email')
# 			# send_mail(
#             #     'Guest Order [' + name + ']',
#             #     name + ', Your order has been received. If you have not paid you can follow this link www.buildqwik.ng/products/product/guest-pay/ to do so',
#             #     'yustaoab@gmail.com',
# 			# 	[email],
#             #     fail_silently=False
#             # )
# 			messages.success(request, "Your order has been placed! Please make payment below")
# 			return redirect('guest_pay')
#
# 		elif form.is_valid():
# 			form.save(commit=False).user = request.user
# 			form.save()
# 			customer = Customer.objects.get(user=request.user)
# 			# first_name = customer.user.first_name
# 			# last_name = customer.user.last_name
# 			# email = customer.user.email
# 			# send_mail(
#             #     'Registered User [' + first_name + ' ' + last_name + ']',
#             #     first_name + ', Your order has been received. Remember you can always log in and checkout to pay from your dashboard',
#             #     'yustaoab@gmail.com',
# 			# 	[email],
#             #     fail_silently=False
#             # )
# 			messages.success(request, "Order submitted! You can checkout below")
# 			return redirect('orders')
# 		else:
# 			messages.error(request, "Please make sure you don't enter too much characters than necessary")
# 	context = {'products': products, 'form': form, 'guest_form': guest_form}
# 	return render(request, 'product/store.html', context)
#
# @login_required
# def fundWallet(request, **kwargs):
# 	form = CustomerCreditForm()
# 	if request.method == 'POST':
# 		form = CustomerCreditForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save(commit=False).user = request.user
# 			form.save()
# 			customer = Customer.objects.get(user=request.user)
# 			first_name = customer.user.first_name
# 			last_name = customer.user.last_name
# 			email = customer.user.email
# 			send_mail(
#                 'Credit Wallet [' + first_name + ' ' + last_name + ']',
#                 first_name + ', Your request has been received! Your wallet will be funded as soon as your payment is verified',
#                 'yustaoab@gmail.com',
# 				[email],
#                 fail_silently=False
#             )
# 			messages.success(request, "Request Submitted, Your wallet will be funded as soon as your payment is verified")
# 			return redirect('dashboard')
# 		else:
# 			messages.error(request, "Please make sure you don't enter too much characters than necessary")
# 	context = {'form': form}
# 	return render(request, 'product/customercredit_form.html', context)
