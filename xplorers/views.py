from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Full, ThreeQuarter, OneQuarter
from datetime import date

def showXplore(request):
    fulls = Full.objects.filter(expiry__gte=date.today())
    three_quarters = ThreeQuarter.objects.filter(expiry__gte=date.today())
    one_quarters = OneQuarter.objects.filter(expiry__gte=date.today())
    context = {'fulls': fulls, 'three_quarters': three_quarters, 'one_quarters': one_quarters}
    return render(request, 'xplorers/xplore.html', context)

@login_required
def showXploreDashboard(request):
    return render(request, 'xplorers/xplore_dashboard.html')#, context)
