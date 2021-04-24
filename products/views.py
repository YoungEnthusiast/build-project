from django.shortcuts import render, redirect, get_object_or_404
from  .models import Category, Product, ProductCredit
from orders.models import VisitorOrder, UserOrder
from .forms import ProductCreditForm
from orders.forms import VisitorOrderForm, UserOrderForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from users.models import ProductCustomer
import random

from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/store.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

# def showProduct(request):
# 	products = Product.objects.all()
# 	form = UserOrderForm()
# 	guest_form = VisitorOrderForm()
# 	if request.method == 'POST' and request.user.is_authenticated == True:
# 		form = UserOrderForm(request.POST or None)
# 		if form.is_valid():
# 			form.save(commit=False).user = request.user
# 			form.save()
# 			reg = UserOrder.objects.filter(order_Id=2021)[0]
# 			reg.order_Id = "BQ" + str(random.randint(10000000,99999999))
# 			if reg.state == "Select a State":
# 				reg.state = reg.user.productcustomer.state
# 			if reg.email == "":
# 				reg.email = reg.user.email
# 			if reg.phone_Number == "":
# 				reg.phone_Number = reg.user.productcustomer.phone_Number
# 			if reg.city == "":
# 				reg.city = reg.user.productcustomer.city
# 			if reg.address == "":
# 				reg.address = reg.user.productcustomer.address
# 			reg.save()
# 			customer = ProductCustomer.objects.get(user=request.user)
# 			first_name = customer.user.first_name
# 			last_name = customer.user.last_name
# 			email = customer.user.email
# 			# send_mail(
# 			# 	'Registered User [' + str(first_name) + ' ' + str(last_name) + ']',
# 			# 	'Dear ' + str(first_name) + ', your order has been received. Remember you can always log in and checkout to pay from your dashboard',
# 			# 	'support@buildqwik.ng',
# 			# 	[email, 'support@buildqwik.ng'],
# 			# 	fail_silently=False
# 			# )
# 			messages.success(request, "Order submitted! You can checkout below")
# 			return redirect('orders')
# 		else:
# 			messages.error(request, "Order is not yet placed successfully")
#
# 	if request.method == 'POST' and request.user.is_authenticated == False:
# 		guest_form = VisitorOrderForm(request.POST or None)
# 		if guest_form.is_valid():
# 			guest_form.save()
# 			visitor = VisitorOrder.objects.filter(order_Id=2021)[0]
# 			visitor.order_Id = "BQ" + str(random.randint(10000000,99999999))
# 			visitor.save()
# 			name = guest_form.cleaned_data.get('name')
# 			email = guest_form.cleaned_data.get('email')
# 			# send_mail(
# 			# 	'Guest Order [' + str(name) + ']',
# 			# 	'Dear ' + str(name) + ', your order has been received. The ORDER ID is: ' + visitor.order_Id + '. If you have not paid you can follow this link www.buildqwik.ng/visitor-pay/ to do so',
# 			# 	'support@buildqwik.ng',
# 			# 	[email, 'support@buildqwik.ng'],
# 			# 	fail_silently=False
# 			# )
# 			messages.success(request, "Your order has been placed! Please make payment below")
# 			return redirect('guest_pay')
# 		else:
# 			messages.error(request, "Order is not yet placed successfully")
#
# 	context = {'products': products, 'form': form, 'guest_form': guest_form}
# 	return render(request, 'product/store.html', context)

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
                'Wallet Credit Request[' + str(first_name) + ' ' + str(last_name) + ']',
                'Dear ' + str(first_name) + ', Your request has been received! Your wallet will be funded as soon as your payment is verified',
                'support@buildqwik.ng',
				[email, 'support@buildqwik.ng'],
                fail_silently=False
            )
			messages.success(request, "Request Submitted, Your wallet will be funded as soon as your payment is verified")
			return redirect('dashboard')
		else:
			messages.error(request, "Please make sure you don't enter too much characters than necessary")
	context = {'form': form}
	return render(request, 'product/customercredit_form.html', context)
