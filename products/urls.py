from django.urls import path
from products import views

urlpatterns = [
    #path('product/', views.showProduct, name='product'),
    path('product', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('fund-wallet/', views.fundWallet, name='fund'),
]
