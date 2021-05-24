from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, UserOrder, VisitorOrder, VisitorOrderItem, UserOrderStatus
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserOrderForm, VisitorOrderForm, AddOrderForm
from cart.cart import Cart
import random
from users.models import ProductCustomer
from django.contrib.auth.decorators import login_required, permission_required
from django.template.loader import render_to_string

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST' and request.user.is_authenticated == True:
        form = UserOrderForm(request.POST)
        if form.is_valid():
            form.save(commit=False).user = request.user
            order = form.save()
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
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            customer = ProductCustomer.objects.get(user=request.user)
            first_name = customer.user.first_name
            last_name = customer.user.last_name
            email = form.cleaned_data.get('email')
            send_mail(
                'Registered User [' + str(first_name) + ' ' + str(last_name) + ']',
                'Dear ' + str(first_name) + ', your order has been received. Remember you can always log in and checkout to pay from your dashboard',
                'admin@buildqwik.ng',
                [email, 'support@buildqwik.ng'],
                fail_silently=False,
                html_message = render_to_string('orders/order_email.html')
            )
            messages.success(request, "Order completed! You can checkout below")
            return redirect('orders')
        else:
            messages.error(request, "Please review form input fields below")
    else:
        form = UserOrderForm()
    return render(request, 'orders/create.html', {'cart': cart,
                                                        'form': form})

def order_visitor(request):
    cart = Cart(request)
    if request.method == 'POST' and request.user.is_authenticated == False:
        guest_form = VisitorOrderForm(request.POST)
        if guest_form.is_valid():
            order = guest_form.save()
            visitor = VisitorOrder.objects.filter(order_Id=2021)[0]
            visitor.order_Id = "BQ" + str(random.randint(10000000,99999999))
            visitor.save()
            for item in cart:
                VisitorOrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            name = guest_form.cleaned_data.get('first_Name')
            email = guest_form.cleaned_data.get('email')
            send_mail(
            	'Guest Order [' + str(name) + ']',
            	'Dear ' + str(name) + ', your order has been received. The ORDER ID is: ' + visitor.order_Id + '. If you have not paid you can follow this link www.buildqwik.ng/visitor-pay/ to do so',
            	'admin@buildqwik.ng',
            	[email, 'support@buildqwik.ng'],
            	fail_silently=False,
                html_message = render_to_string('orders/order_email2.html', {'name': str(name), 'order_Id': visitor.order_Id})
            )
            messages.success(request, "Your order has been placed! Please make payment below")
            return redirect('guest_pay')
        else:
            messages.error(request, "Please review form input fields below")
    else:
        guest_form = VisitorOrderForm()
    return render(request, 'orders/visitor_create.html', {'cart': cart,
                                                        'guest_form': guest_form})

@login_required
@permission_required('orders.add_UserOrderStatus')
def addOrder(request):
    form = AddOrderForm()
    if request.method == 'POST':
        form = AddOrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            order = form.cleaned_data.get('order')
            status = form.cleaned_data.get('order_Status')
            reg = UserOrder.objects.get(order_Id=order)
            email = reg.user.email
            name = reg.user.first_name
            send_mail(
                'Order Status',
                'Dear ' + str(name) + ', Your order status has now been changed to ' + str(status),
                'admin@buildqwik.ng',
                [email, 'support@buildqwik.ng'],
                fail_silently=False
            )
            messages.success(request, str(name) + "'s Order Status has been updated")
            return redirect('dashboard')
    return render(request, 'orders/addorder_form.html', {'form': form})
