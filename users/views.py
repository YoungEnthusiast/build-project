from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm, ProfileEditForm, CustomerEditForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from cement.models import Cement, CementOrder, GuestCementOrder
from cement.forms import CementOrderForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import DeleteView
from .models import Customer
from cement.filters import CementOrderFilter
from django.core.paginator import Paginator
from django.core.mail import send_mail

def create(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            customer = Customer.objects.create(user=form)
            messages.success(request, "Your account has been created! Please login to complete registration by supplying location information")
            return redirect('edit_profile')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/account.html', {'form': form})

@login_required
def editProfile(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        customer_form = CustomerEditForm(request.POST, instance=request.user.customer)
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

@login_required
def showDashboard(request):
    context = {}
    filtered_cementorders = CementOrderFilter(
        request.GET,
        queryset = CementOrder.objects.filter(user=request.user)
    )
    context['filtered_cementorders'] = filtered_cementorders
    paginated_filtered_cementorders = Paginator(filtered_cementorders.qs, 10)
    page_number = request.GET.get('page')
    cementorders_page_obj = paginated_filtered_cementorders.get_page(page_number)
    context['cementorders_page_obj'] = cementorders_page_obj
    total_cementorders = filtered_cementorders.qs.count()
    context['total_cementorders'] = total_cementorders
    return render(request, 'users/dashboard.html', context=context)

def updateCementOrder(request, id):
    cement_order = CementOrder.objects.get(id=id)
    form = CementOrderForm(instance=cement_order)
    if request.method=='POST':
        form = CementOrderForm(request.POST, instance=cement_order)
        if form.is_valid():
            form.save()
            messages.success(request, "Your order has been modified")
            return redirect('dashboard')
    return render(request, 'cement/cementorder_form.html', {'form': form, 'cement_order': cement_order})

def deleteCementOrder(request, id):
    cement_order = CementOrder.objects.get(id=id)
    obj = get_object_or_404(CementOrder, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('dashboard')
    context = {'cement_order': cement_order}
    return render(request, 'cement/cementorder_confirm_delete.html', context)
    # def handler403(request, exception, template_name='403.html'):
    #     return render(request, '403.html')

def selectCementOrder(request, id):
    cement_order = CementOrder.objects.get(id=id)
    cement_order.checkout = True
    cement_order.save()
    messages.success(request, "Order selected")
    return redirect('dashboard')

def deSelectCementOrder(request, id):
    cement_order = CementOrder.objects.get(id=id)
    cement_order.checkout = False
    cement_order.save()
    messages.success(request, "Order deselected")
    return redirect('dashboard')

def showCementOrder(request, pk, **kwargs):
    cement_order = CementOrder.objects.get(id=pk)
    context = {'cement_order': cement_order}
    return render(request, 'cement/cementorder_detail.html', context)

def showCementOrder2(request):
    that = CementOrder.objects.filter(user=request.user, checkout=True)
    response_that = []
    for each in that:
        selected = CementOrder.objects.filter(user=request.user, checkout=True)
        tot = 0
        for a_cement in selected:
            tot = tot + a_cement.total_price
        response_that.append(each)
    return render(request, 'cement/cementorder_detail2.html', {'that': response_that, 'tot':tot})

def updateWallet(request, pk, **kwargs):
    cement_order = CementOrder.objects.get(id=pk)
    wallet = Customer.objects.get(user=request.user)
    wallet.wallet = wallet.wallet - cement_order.total_price
    if wallet.wallet > 0:
        wallet.save()
        messages.success(request, "Your payment has been made and your wallet updated")
        cement_order.payment_status = "Confirmed"
        cement_order.checkout = False
        cement_order.save()
        return redirect('dashboard')
    else:
        messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")

    context = {'cement_order': cement_order, 'wallet': wallet}
    return render(request, 'cement/wallet.html', context)

def updateWallet2(request):
    that = CementOrder.objects.filter(user=request.user, checkout=True)
    response_that = []
    for each in that:
        selected = CementOrder.objects.filter(user=request.user, checkout=True)
        tot = 0
        for a_cement in selected:
            tot = tot + a_cement.total_price

    wallet = Customer.objects.get(user=request.user)
    wallet.wallet = wallet.wallet - tot
    if wallet.wallet > 0:
        wallet.save()
        messages.success(request, "Your payment has been made and your wallet updated")
        for each2 in that:
            each2.payment_status = "Confirmed"
            each2.checkout = False
            each2.save()
        return redirect('dashboard')
    else:
        messages.error(request, "Wallet balance is not enough to perform this transaction. Please fund your wallet")
    response_that.append(each)
    context = {'that': response_that, 'tot':tot, 'wallet': wallet}
    return render(request, 'cement/wallet.html', context)

def guestPay(request):
    return render(request, 'cement/cementorder_guest.html')
