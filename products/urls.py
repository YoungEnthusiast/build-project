from django.urls import path
from products import views

urlpatterns = [
    path('product/', views.showProduct, name='product'),
    path('fund-wallet/', views.fundWallet, name='fund'),
]
