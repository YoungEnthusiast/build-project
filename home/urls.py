from django.urls import path
from home import views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('about-buildqwik', views.showAbout, name='about'),
    path('terms-and-conditions', views.showTerms, name='terms'),
    path('return-policy', views.showReturn, name='return'),
    path('contact-us', views.showContact, name='contact'),
]
