from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Full, ThreeQuarter, OneQuarter, Subscription, Request
from datetime import date
from .filters import SubscriptionFilter
from django.core.paginator import Paginator
from .forms import RequestForm
from users.models import ProductCustomer
from django.core.mail import send_mail
from django.contrib import messages

def showXplore(request):
    fulls = Full.objects.filter(expiry__gte=date.today())
    three_quarters = ThreeQuarter.objects.filter(expiry__gte=date.today())
    one_quarters = OneQuarter.objects.filter(expiry__gte=date.today())
    context = {'fulls': fulls, 'three_quarters': three_quarters, 'one_quarters': one_quarters}
    return render(request, 'xplorers/xplore.html', context)

@login_required
def showXploreDashboard(request):
    return render(request, 'xplorers/xplore_dashboard.html')#, context)

@login_required
def showSubscriptions(request):
    context = {}
    filtered_subscriptions = SubscriptionFilter(
        request.GET,
        queryset = Subscription.objects.filter(xplorer__user=request.user)
    )
    context['filtered_subscriptions'] = filtered_subscriptions
    paginated_filtered_subscriptions = Paginator(filtered_subscriptions.qs, 10)
    page_number = request.GET.get('page')
    subscriptions_page_obj = paginated_filtered_subscriptions.get_page(page_number)
    context['subscriptions_page_obj'] = subscriptions_page_obj
    total_subscriptions = filtered_subscriptions.qs.count()
    context['total_subscriptions'] = total_subscriptions
    return render(request, 'xplorers/subscriptions.html', context=context)

@login_required
def uploadRequest(request, **kwargs):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save()
            customer = ProductCustomer.objects.get(user=request.user)
            first_name = customer.user.first_name
            last_name = customer.user.last_name
            email = customer.user.email
            send_mail(
                'Advert Request[' + str(first_name) + ' ' + str(last_name) + ']',
                'Dear ' + str(first_name) + ', Your request has been received! Your advert will be activated as soon as your payment is verified',
                'admin@buildqwik.ng',
				[email, 'payment@buildqwik.ng'],
                fail_silently=False
            )
            messages.success(request, "Request Submitted, Your advert will be activated as soon as your payment is verified")
            return redirect('xplore-dashboard')
        else:
            messages.error(request, "Please make sure you don't enter too much characters than necessary")
    context = {'form': form}
    return render(request, 'xplorers/request_form.html', context)
