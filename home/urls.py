from django.urls import path
from home import views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('about-buildqwik', views.showAbout, name='about'),
    path('terms-and-conditions-of-sales', views.showTerms, name='terms'),
    path('terms-and-conditions-of-website-use', views.showTerms2, name='terms2'),
    path('return-policy', views.showReturn, name='return'),
    path('contact-us', views.showContact, name='contact'),
]
