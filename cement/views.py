from django.shortcuts import render, redirect
from  .models import Cement, CementOrder
from .forms import CementOrderForm, GuestCementOrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def showCement(request):
	cements = Cement.objects.all()
	form = CementOrderForm()
	guest_form = GuestCementOrderForm()
	if request.method == 'POST':
		form = CementOrderForm(request.POST or None)
		guest_form = GuestCementOrderForm(request.POST or None)
		if guest_form.is_valid():
			guest_form.save()
			messages.success(request, "Order submitted!")
			
		elif form.is_valid():
			form.save(commit=False).user = request.user
			form.save()
			messages.success(request, "Order submitted! You can checkout below")
			return redirect('dashboard')
		else:
			messages.error(request, "ERROR: Please make sure you don't enter too much characters than necessary")
	context = {'cements': cements, 'form': form, 'guest_form': guest_form}
	return render(request, 'cement/store.html', context)
