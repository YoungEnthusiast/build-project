from django.urls import path
from xplorers import views

urlpatterns = [
path('xplore', views.showXplore, name='xplore'),
path('xplordash', views.showXploreDashboard, name='xplore-dashboard'),
path('subscriptions', views.showSubscriptions, name='subscriptions'),
path('advert-request', views.uploadRequest, name='request'),
]
