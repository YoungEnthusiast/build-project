import json
import urllib.request
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm, ProfileEditForm, ProductCustomerEditForm, AdminCreditForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from orders.models import UserOrder, VisitorOrder, OrderItem, VisitorOrderItem
from products.models import Product
from products.filters import UserOrderFilter, UserOrderFilter2
from orders.forms import UserOrderForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required
from .models import ProductCustomer, ProductWalletHistorie
from xplorers.models import XploreCustomer
from .filters import ProductWalletHistorieFilter
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.views.generic import View, UpdateView
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def create(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate Your BuildQwik Account'
                message = render_to_string('users/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                messages.success(request, ('Please login to your email, you have been sent a message for your email verification.'))
                return redirect('login')
            else:
                messages.error(request, "Please ensure you pass reCAPTCHA so as to ascertain that you are human")
            return redirect('account')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/account.html', {'form': form})

# def create(request):
#     if request.method == "POST":
#         form = CustomRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your BuildQwik Account'
#             message = render_to_string('users/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             messages.success(request, ('Please login to your email, you have been sent a message for your email verification.'))
#             return redirect('login')
#             #return redirect('edit_profile')
#         else:
#             messages.error(request, 'A user with the supplied username or email already exists')
#         return redirect('account')
#     else:
#         form = CustomRegisterForm()
#     return render(request, 'users/account.html', {'form': form})

class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.productcustomer.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account has been confirmed! Please complete registration by supplying location information'))
            return redirect('edit_profile')
        else:
            messages.warning(request, ('The confirmation link has either been used or expired.'))
            return redirect('index')

@login_required
def editProfile(request, **kwargs):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        customer_form = ProductCustomerEditForm(request.POST, request.FILES, instance=request.user.productcustomer)
        if form.is_valid() and customer_form.is_valid():
            form.save()
            customer_form.save()
            new_customer = ProductCustomer.objects.get(user=request.user)
            new_customer.save()
            try:
                if new_customer.CAC_Certificate == "":
                    pass
                else:
                    new_xplorer = XploreCustomer()
                    new_xplorer.user = new_customer.user
                    new_xplorer.phone_Number = new_customer.phone_Number
                    new_xplorer.state = new_customer.state
                    new_xplorer.city = new_customer.city
                    new_xplorer.address = new_customer.address
                    new_xplorer.CAC_Certificate = new_customer.CAC_Certificate
                    new_xplorer.save()
            except:
                new_xplorer = XploreCustomer.objects.get(user=request.user)
                new_xplorer.user = new_customer.user
                new_xplorer.phone_Number = new_customer.phone_Number
                new_xplorer.state = new_customer.state
                new_xplorer.city = new_customer.city
                new_xplorer.address = new_customer.address
                new_xplorer.CAC_Certificate = new_customer.CAC_Certificate
                new_xplorer.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('edit_profile')
        else:
            messages.error(request, "Error updating your profile")
    else:
        form = ProfileEditForm(instance=request.user)
        customer_form = ProductCustomerEditForm(instance=request.user.productcustomer)
    return render(request, 'users/edit_profile.html', {'form': form, 'customer_form': customer_form})

@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            user = request.user
            name = user.first_name
            email = user.email
            send_mail(
                'Password Changed!',
                'Dear ' + str(name) + ', your password has just been changed. If this activity was not carried out by you, please reply to this email',
                'support@buildqwik.ng',
                [email],
                fail_silently=False
            )
            messages.success(request, "Your password has been changed successfully")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def showDashboard(request):
    new_orders = UserOrder.objects.filter(user=request.user, order_Status = 'New')
    new = new_orders.count()
    pending_orders = UserOrder.objects.filter(user=request.user, order_Status = 'Pending')
    pending = pending_orders.count()
    completed_orders = UserOrder.objects.filter(user=request.user, order_Status = 'Completed')
    completed = completed_orders.count()
    total_debited = ProductWalletHistorie.objects.filter(user=request.user).aggregate(Sum('amount_debited'))['amount_debited__sum']
    try:
        wallet = ProductWalletHistorie.objects.filter(user=request.user)[0]
        last_tran = wallet.last_tran
        current_balance = wallet.current_balance
    except:
        last_tran = "---"
        current_balance = "---"

    context = {'new': new, 'pending': pending, 'completed': completed,
                'total_debited': total_debited, 'last_tran': last_tran, 'current_balance':current_balance}
    return render(request, 'users/dashboard.html', context)

@login_required
def showXploreDashboard(request):

    return render(request, 'xplorers/xplore_dashboard.html')#, context)

@login_required
def showOrders(request):
    context = {}
    filtered_productorders = UserOrderFilter(
        request.GET,
        queryset = UserOrder.objects.filter(user=request.user)
    )
    context['filtered_productorders'] = filtered_productorders
    paginated_filtered_productorders = Paginator(filtered_productorders.qs, 10)
    page_number = request.GET.get('page')
    productorders_page_obj = paginated_filtered_productorders.get_page(page_number)
    context['productorders_page_obj'] = productorders_page_obj
    total_productorders = filtered_productorders.qs.count()
    context['total_productorders'] = total_productorders
    return render(request, 'users/orders.html', context=context)

@login_required
def showInvoices(request):
    context = {}
    filtered_productinvoices = UserOrderFilter2(
        request.GET,
        queryset = UserOrder.objects.filter(user=request.user, payment_Status='Confirmed')
    )
    context['filtered_productinvoices'] = filtered_productinvoices
    paginated_filtered_productinvoices = Paginator(filtered_productinvoices.qs, 10)
    page_number = request.GET.get('page')
    productinvoices_page_obj = paginated_filtered_productinvoices.get_page(page_number)
    context['productinvoices_page_obj'] = productinvoices_page_obj
    total_productinvoices = filtered_productinvoices.qs.count()
    context['total_productinvoices'] = total_productinvoices
    return render(request, 'users/invoice.html', context=context)

@login_required
def updateProductOrder(request, id):
    product_order = UserOrder.objects.get(id=id)
    form = UserOrderForm(instance=product_order)
    if request.method=='POST':
        form = UserOrderForm(request.POST, instance=product_order)
        if form.is_valid():
            form.save()
            messages.success(request, "Your order has been modified")
            return redirect('orders')
    return render(request, 'product/productorder_form.html', {'form': form, 'product_order': product_order})

@login_required
def deleteProductOrder(request, id):
    product_order = UserOrder.objects.get(id=id)
    obj = get_object_or_404(UserOrder, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('orders')
    context = {'product_order': product_order}
    return render(request, 'product/productorder_confirm_delete.html', context)
    # def handler403(request, exception, template_name='403.html'):
    #     return render(request, '403.html')

# @login_required
# def selectProductOrder(request, id):
#     product_order = UserOrder.objects.get(id=id)
#     product_order.checkout_checked = True
#     product_order.save()
#     messages.success(request, "Order selected")
#     return redirect('orders')
#
# @login_required
# def deSelectProductOrder(request, id):
#     product_order = UserOrder.objects.get(id=id)
#     product_order.checkout_checked = False
#     product_order.save()
#     messages.success(request, "Order deselected")
#     return redirect('orders')
#
# @login_required
# def selectInvoice(request, id):
#     product_invoice = UserOrder.objects.get(id=id)
#     product_invoice.invoice_checked = True
#     product_invoice.save()
#     messages.success(request, "Invoice selected")
#     return redirect('invoices')
#
# @login_required
# def deSelectInvoice(request, id):
#     product_invoice = UserOrder.objects.get(id=id)
#     product_invoice.invoice_checked = False
#     product_invoice.save()
#     messages.success(request, "Invoice deselected")
#     return redirect('invoices')

@login_required
def showProductOrder(request, pk, **kwargs):
    product_order = UserOrder.objects.get(id=pk)
    order_items = OrderItem.objects.filter(order__id=pk)

    context = {'product_order': product_order, 'order_items': order_items}
    return render(request, 'product/productorder_detail.html', context)

@login_required
def showInvoice(request, pk, **kwargs):
    product_invoice = UserOrder.objects.get(id=pk)
    order_items = OrderItem.objects.filter(order__id=pk)

    context = {'product_invoice': product_invoice, 'order_items': order_items}
    return render(request, 'users/invoice2.html', context)

# @login_required
# def showInvoiceMany(request):
#     the_user = UserOrder.objects.filter(user=request.user, invoice_checked=True)[0]
#     that = UserOrder.objects.filter(user=request.user, invoice_checked=True)
#     response_that = []
#     for each in that:
#         selected = UserOrder.objects.filter(user=request.user, invoice_checked=True)
#         tot = 0
#         for a_product in selected:
#             tot = tot + a_product.total_Price
#         response_that.append(each)
#
#     context = {'that': response_that, 'tot':tot, 'the_user': the_user}
#     return render(request, 'users/invoice3.html', context)

# @login_required
# def showProductOrder2(request):
#     that = UserOrder.objects.filter(user=request.user, checkout_checked=True)
#     user = request.user
#     email = user.email
#     response_that = []
#     for each in that:
#         selected = UserOrder.objects.filter(user=request.user, checkout_checked=True)
#         tot = 0
#         for a_product in selected:
#             tot = tot + a_product.get_total_cost
#         response_that.append(each)
#     return render(request, 'product/productorder_detail2.html', {'email': email, 'that': response_that, 'tot':tot})

@login_required
def updateWallet(request, pk, **kwargs):
    try:
        product_order = UserOrder.objects.get(id=pk)
        wallet = ProductWalletHistorie.objects.filter(user=request.user)[0]
        wallet.current_balance = wallet.current_balance - product_order.get_total_cost()
        wallet.amount_debited = product_order.get_total_cost()
        if wallet.current_balance > 0:
            wallet_entry = ProductWalletHistorie()
            wallet_entry.user = wallet.user
            wallet_entry.amount_debited = wallet.amount_debited
            wallet_entry.current_balance = wallet.current_balance
            wallet_entry.last_tran = wallet_entry.amount_debited
            wallet_entry.save()
            messages.success(request, "Your payment has been made and your wallet updated")
            product_order.payment_Status = "Confirmed"
            product_order.checkout_checked = False
            product_order.save()
            return redirect('orders')
        else:
            messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
        context = {'product_order': product_order, 'wallet': wallet_entry}
        return render(request, 'product/wallet.html', context)
    except:
        messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
        return render(request, 'product/wallet.html')

# @login_required
# def updateWallet2(request):
#     try:
#         that = UserOrder.objects.filter(user=request.user, checkout_checked=True)
#         response_that = []
#         for each in that:
#             selected = UserOrder.objects.filter(user=request.user, checkout_checked=True)
#             tot = 0
#             for a_product in selected:
#                 tot = tot + a_product.total_Price
#         wallet = ProductWalletHistorie.objects.filter(user=request.user)[0]
#         wallet.current_balance = wallet.current_balance - tot
#         wallet.amount_debited = tot
#         if wallet.current_balance > 0:
#             wallet_entry = ProductWalletHistorie()
#             wallet_entry.user = wallet.user
#             wallet_entry.amount_debited = wallet.amount_debited
#             wallet_entry.current_balance = wallet.current_balance
#             wallet_entry.last_tran = wallet_entry.amount_debited
#             wallet_entry.save()
#             messages.success(request, "Your payment has been made and your wallet updated")
#             for each2 in that:
#                 each2.payment_Status = "Confirmed"
#                 each2.checkout_checked = False
#                 each2.save()
#             return redirect('orders')
#         else:
#             messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
#         response_that.append(each)
#         context = {'that': response_that, 'tot':tot, 'wallet': wallet}
#         return render(request, 'product/wallet.html', context)
#     except:
#         messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
#         return render(request, 'product/wallet.html')

def guestPay(request):
    visitor = VisitorOrder.objects.all()[0]
    order_Id = visitor.order_Id
    id = visitor.id
    order_items = VisitorOrderItem.objects.filter(order__id=id)
    email = visitor.email
    total_Price = visitor.get_total_cost()
    context = {'order_Id': order_Id,  'email': email, 'total_Price': total_Price, 'order_items': order_items}
    return render(request, 'product/productorder_guest.html', context)

def visitorPay(request):
    return render(request, 'product/productorder_visitor.html')

@login_required
def showWallet(request):
    context = {}
    filtered_wallets = ProductWalletHistorieFilter(
        request.GET,
        queryset = ProductWalletHistorie.objects.filter(user=request.user)
    )
    context['filtered_wallets'] = filtered_wallets
    paginated_filtered_wallets = Paginator(filtered_wallets.qs, 10)
    page_number = request.GET.get('page')
    wallets_page_obj = paginated_filtered_wallets.get_page(page_number)
    context['wallets_page_obj'] = wallets_page_obj
    total_wallets = filtered_wallets.qs.count()
    context['total_wallets'] = total_wallets
    return render(request, 'users/wallet_history.html', context=context)

@login_required
@permission_required('home.add_ProductWalletHistorie')
def creditWallet(request):
    form = AdminCreditForm()
    if request.method == 'POST':
        form = AdminCreditForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('user')
            wallet_0 = ProductWalletHistorie.objects.filter(user=name)[0]
            try:
                wallet_1 = ProductWalletHistorie.objects.filter(user=name)[1]
                wallet_0.current_balance = wallet_0.amount_credited + wallet_1.current_balance
                wallet_0.last_tran = wallet_0.amount_credited
                email = wallet_0.user.email
                wallet_0.save()
                send_mail(
                    'Wallet Credit Confirmed',
                    'Dear ' + str(name) + ', Your wallet balance has been topped up',
                    'support@buildqwik.ng',
    				[email],
                    fail_silently=False
                )
                messages.success(request, str(name) + "'s wallet balance has been topped up and email notification sent to him")
                return redirect('dashboard')
            except:
                wallet_0.current_balance = wallet_0.amount_credited
                wallet_0.last_tran = wallet_0.amount_credited
                email = wallet_0.user.email
                wallet_0.save()
                send_mail(
                    'Wallet Credit Confirmed',
                    'Dear ' + str(name) + ', Your wallet balance has been topped up',
                    'support@buildqwik.ng',
    				[email],
                    fail_silently=False
                )
                messages.success(request, str(name) + "'s wallet balance has been topped up and email notification sent to him")
                return redirect('dashboard')
    return render(request, 'product/admincredit_form.html', {'form': form})
