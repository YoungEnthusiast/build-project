from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription, Request
from datetime import date
from .filters import SubscriptionFilter
from django.core.paginator import Paginator
from .forms import RequestForm
from users.models import ProductCustomer
from django.core.mail import send_mail
from django.contrib import messages

def showXplore(request):
    fulls = Subscription.objects.filter(package='Full Width', subscription_Ends__gte=date.today())
    three_quarters = Subscription.objects.filter(package='Three Quarters', subscription_Ends__gte=date.today())
    one_quarters = Subscription.objects.filter(package='One Quarter', subscription_Ends__gte=date.today())
    context = {'fulls': fulls, 'three_quarters': three_quarters, 'one_quarters': one_quarters}
    return render(request, 'xplorers/xplore.html', context)

@login_required
def showXploreDashboard(request):
    inactive = Subscription.objects.filter(xplorer__user=request.user, subscription_Ends__lt=date.today()).count()
    active = Subscription.objects.filter(xplorer__user=request.user, subscription_Ends__gte=date.today()).count()
    try:
        expiry = Subscription.objects.filter(xplorer__user=request.user, subscription_Ends__gte=date.today()).order_by('subscription_Ends')[0]
    except:
        expiry = ""

    context = {'inactive': inactive, 'active': active, 'expiry': expiry}
    return render(request, 'xplorers/xplore_dashboard.html', context)

    # new_orders = UserOrder.objects.filter(user=request.user, order_Status = 'New')
    # new = new_orders.count()
    # pending_orders = UserOrder.objects.filter(user=request.user, order_Status = 'Pending')
    # pending = pending_orders.count()
    # completed_orders = UserOrder.objects.filter(user=request.user, order_Status = 'Completed')
    # completed = completed_orders.count()
    # total_debited = ProductWalletHistorie.objects.filter(user=request.user).aggregate(Sum('amount_debited'))['amount_debited__sum']
    # try:
    #     wallet = ProductWalletHistorie.objects.filter(user=request.user)[0]
    #     last_tran = wallet.last_tran
    #     current_balance = wallet.current_balance
    # except:
    #     last_tran = "---"
    #     current_balance = "---"
    #
    # context = {'new': new, 'pending': pending, 'completed': completed,
    #             'total_debited': total_debited, 'last_tran': last_tran, 'current_balance':current_balance}
    # return render(request, 'users/dashboard.html', context)

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
            reg = Request.objects.all()[0]
            if reg.payment_Evidence == "" and reg.waiver_Code == "":
                reg.delete()
                messages.error(request, "Please upload a payment evidence or use a waiver code")
            else:
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
