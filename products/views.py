from django.shortcuts import render, redirect, get_object_or_404
from  .models import Category, Product, ProductCredit
from orders.models import VisitorOrder, UserOrder
from .forms import ProductCreditForm
from orders.forms import VisitorOrderForm, UserOrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from users.models import ProductCustomer
import random
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/store.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

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
                'admin@buildqwik.ng',
				[email, 'payment@buildqwik.ng'],
                fail_silently=False
            )
			messages.success(request, "Request Submitted, Your wallet will be funded as soon as your payment is verified")
			return redirect('dashboard')
		else:
			messages.error(request, "Please make sure you don't enter too much characters than necessary")
	context = {'form': form}
	return render(request, 'product/customercredit_form.html', context)
