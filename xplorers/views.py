from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Full, ThreeQuarter, OneQuarter

def showXplore(request):
    fulls = Full.objects.all()
    three_quarters = ThreeQuarter.objects.all()
    one_quarters = OneQuarter.objects.all()
    context = {'fulls': fulls, 'three_quarters': three_quarters, 'one_quarters': one_quarters}
    return render(request, 'xplorers/xplore.html', context)

@login_required
def showXploreDashboard(request):
    return render(request, 'xplorers/xplore_dashboard.html')#, context)
