from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, ProfileEditForm, CustomerEditForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from cement.models import Cement, CementOrder
from cement.forms import CementOrderForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required
from .models import Customer


def create(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            customer = Customer.objects.create(user=form)
            #user = form.cleaned_data.get('username')
            #messages.error(request, "Testing...")
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
    cements = Cement.objects.all()
    cement_orders = CementOrder.objects.filter(user=request.user)
    context = {'cements': cements, 'cement_orders': cement_orders}
    return render(request, 'users/dashboard.html', context)

@login_required
def updateCementOrder(request, id):
    cement_order = CementOrder.objects.get(id=id)
    form = CementOrderForm(instance=cement_order)
    if request.method=='POST':
        form = CementOrderForm(request.POST, instance=cement_order)
        if form.is_valid():
            form.save()
            messages.success(request, "Your order has been modified")
            return redirect('dashboard')
    return render(request, 'cement/cementorder_form.html', {'form': form})

@login_required
def showCementOrder(request, pk):
    cement_order = CementOrder.objects.get(id=pk)
    context = {'cement_order': cement_order}
    return render(request, 'cement/cementorder_detail.html', context)
