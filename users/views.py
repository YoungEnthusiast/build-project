import json
import urllib.request
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm, ProfileEditForm, ProductCustomerEditForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from product.models import Product, ProductOrder, GuestProductOrder
# from product.forms import ProductOrderForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import DeleteView
from .models import ProductCustomer#, WalletHistory
#from .filters import WalletHistoryFilter
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponseRedirect

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
                form = form.save(commit=False)
                form.save()
                customer = Customer.objects.create(user=form)
                messages.success(request, "Your account has been created! Please login to complete registration by supplying location information")
                return redirect('edit_profile')
            else:
                messages.error(request, 'Please ensure you pass reCAPTCHA to ascertain that you are not a robot')
            return redirect('account')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/account.html', {'form': form})

@login_required
def editProfile(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        customer_form = ProductCustomerEditForm(request.POST, instance=request.user.customer)
        if form.is_valid() and customer_form.is_valid():
            form.save()
            customer_form.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('edit_profile')
        else:
            messages.error(request, "Error updating your profile")
    else:
        form = ProfileEditForm(instance=request.user)
        customer_form = CustomerEditForm(instance=request.user.customer)
    return render(request, 'users/edit_profile.html', {'form': form, 'customer_form': customer_form})

@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been changed successfully")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

# @login_required
# def showDashboard(request):
#     new_orders = ProductOrder.objects.filter(user=request.user, order_status = 'New')
#     new = new_orders.count()
#     pending_orders = ProductOrder.objects.filter(user=request.user, order_status = 'Pending')
#     pending = pending_orders.count()
#     completed_orders = ProductOrder.objects.filter(user=request.user, order_status = 'Completed')
#     completed = completed_orders.count()
#
#     total_debited = WalletHistory.objects.filter(user=request.user).aggregate(Sum('amount_debited'))['amount_debited__sum']
#     try:
#         wallet = WalletHistory.objects.filter(user=request.user)[0]
#         last_tran = wallet.amount_debited
#         current_balance = wallet.current
#     except:
#         last_tran = "---"
#         current_balance = "---"
#
#     context = {'new': new, 'pending': pending, 'completed': completed,
#                 'total_debited': total_debited, 'last_tran': last_tran, 'current_balance':current_balance}
#     return render(request, 'users/dashboard.html', context)
#
# @login_required
# def showOrders(request):
#     context = {}
#     filtered_productorders = ProductOrderFilter(
#         request.GET,
#         queryset = ProductOrder.objects.filter(user=request.user)
#     )
#     context['filtered_productorders'] = filtered_productorders
#     paginated_filtered_productorders = Paginator(filtered_productorders.qs, 10)
#     page_number = request.GET.get('page')
#     productorders_page_obj = paginated_filtered_productorders.get_page(page_number)
#     context['productorders_page_obj'] = productorders_page_obj
#     total_productorders = filtered_productorders.qs.count()
#     context['total_productorders'] = total_productorders
#     return render(request, 'users/orders.html', context=context)
#
# @login_required
# def showInvoices(request):
#     context = {}
#     filtered_productorders = ProductOrderFilter2(
#         request.GET,
#         queryset = ProductOrder.objects.filter(user=request.user, payment_status='Confirmed')
#     )
#     context['filtered_productorders'] = filtered_productorders
#     paginated_filtered_productorders = Paginator(filtered_productorders.qs, 10)
#     page_number = request.GET.get('page')
#     productorders_page_obj = paginated_filtered_productorders.get_page(page_number)
#     context['productorders_page_obj'] = productorders_page_obj
#     total_productorders = filtered_productorders.qs.count()
#     context['total_productorders'] = total_productorders
#     return render(request, 'users/invoice.html', context=context)
#
# @login_required
# def updateProductOrder(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     form = ProductOrderForm(instance=product_order)
#     if request.method=='POST':
#         form = ProductOrderForm(request.POST, instance=product_order)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your order has been modified")
#             return redirect('orders')
#     return render(request, 'product/productorder_form.html', {'form': form, 'product_order': product_order})
#
# @login_required
# def deleteProductOrder(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     obj = get_object_or_404(ProductOrder, id = id)
#     if request.method =="POST":
#         obj.delete()
#         return redirect('orders')
#     context = {'product_order': product_order}
#     return render(request, 'product/productorder_confirm_delete.html', context)
#     # def handler403(request, exception, template_name='403.html'):
#     #     return render(request, '403.html')
#
# @login_required
# def selectProductOrder(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     product_order.checkout = True
#     product_order.save()
#     messages.success(request, "Order selected")
#     return redirect('orders')
#
# @login_required
# def deSelectProductOrder(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     product_order.checkout = False
#     product_order.save()
#     messages.success(request, "Order deselected")
#     return redirect('orders')
#
# @login_required
# def selectInvoice(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     product_order.checkout = True
#     product_order.save()
#     messages.success(request, "Order selected")
#     return redirect('invoices')
#
# @login_required
# def deSelectInvoice(request, id):
#     product_order = ProductOrder.objects.get(id=id)
#     product_order.checkout = False
#     product_order.save()
#     messages.success(request, "Order deselected")
#     return redirect('invoices')
#
# @login_required
# def showProductOrder(request, pk, **kwargs):
#     product_order = ProductOrder.objects.get(id=pk)
#     context = {'product_order': product_order}
#     return render(request, 'product/productorder_detail.html', context)
#
# @login_required
# def showProductOrder2(request):
#     that = ProductOrder.objects.filter(user=request.user, checkout=True)
#     response_that = []
#     for each in that:
#         selected = ProductOrder.objects.filter(user=request.user, checkout=True)
#         tot = 0
#         for a_product in selected:
#             tot = tot + a_product.total_price
#         response_that.append(each)
#     return render(request, 'product/productorder_detail2.html', {'that': response_that, 'tot':tot})
#
# @login_required
# def updateWallet(request, pk, **kwargs):
#     product_order = ProductOrder.objects.get(id=pk)
#     wallet = WalletHistory.objects.filter(user=request.user)[0]
#     wallet.current = wallet.current_balance - product_order.total_price
#     wallet.amount_debited = product_order.total_price
#     if wallet.current_balance > 0:
#         wallet_entry = WalletHistory()
#         wallet_entry.user = wallet.user
#         #wallet_entry.customer = wallet.customer
#         wallet_entry.amount_debited = wallet.amount_debited
#         wallet_entry.current = wallet.current_balance
#         #wallet.save()
#         wallet_entry.save()
#         messages.success(request, "Your payment has been made and your wallet updated")
#         product_order.payment_status = "Confirmed"
#         product_order.checkout = False
#         product_order.save()
#         return redirect('orders')
#     else:
#         messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
#     context = {'product_order': product_order, 'wallet': wallet_entry}
#     return render(request, 'product/wallet.html', context)
#
# @login_required
# def updateWallet2(request):
#     that = ProductOrder.objects.filter(user=request.user, checkout=True)
#     response_that = []
#     for each in that:
#         selected = ProductOrder.objects.filter(user=request.user, checkout=True)
#         tot = 0
#         for a_product in selected:
#             tot = tot + a_product.total_price
#     wallet = WalletHistory.objects.filter(user=request.user)[0]
#     wallet.current = wallet.current_balance - tot
#     wallet.amount_debited = tot
#     if wallet.current_balance > 0:
#         wallet_entry = WalletHistory()
#         wallet_entry.user = wallet.user
#         #wallet_entry.customer = wallet.customer
#         wallet_entry.amount_debited = wallet.amount_debited
#         wallet_entry.current = wallet.current_balance
#         wallet_entry.save()
#         messages.success(request, "Your payment has been made and your wallet updated")
#         for each2 in that:
#             each2.payment_status = "Confirmed"
#             each2.checkout = False
#             each2.save()
#         return redirect('orders')
#     else:
#         messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
#     response_that.append(each)
#     context = {'that': response_that, 'tot':tot, 'wallet': wallet}
#     return render(request, 'product/wallet.html', context)
#
# def guestPay(request):
#     return render(request, 'product/productorder_guest.html')
#
# def showWallet(request):
#     context = {}
#     filtered_wallets = WalletHistoryFilter(
#         request.GET,
#         queryset = WalletHistory.objects.filter(user=request.user)
#     )
#     context['filtered_wallets'] = filtered_wallets
#     paginated_filtered_wallets = Paginator(filtered_wallets.qs, 10)
#     page_number = request.GET.get('page')
#     wallets_page_obj = paginated_filtered_wallets.get_page(page_number)
#     context['wallets_page_obj'] = wallets_page_obj
#     total_wallets = filtered_wallets.qs.count()
#     context['total_wallets'] = total_wallets
#     return render(request, 'users/wallet_history.html', context=context)
