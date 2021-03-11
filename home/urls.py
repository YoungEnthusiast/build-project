from django.urls import path
from home import views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('about-buildqwik/', views.showAbout, name='about'),
    path('contact-us/', views.showContact, name='contact'),
    path('st---only/', views.showContacts, name='contacts'),
]
