from django.urls import path
from cement import views

urlpatterns = [
    path('cement/', views.showCement, name='cement'),
    path('fund-wallet/', views.fundWallet, name='fund'),
]
