from django.urls import path
from products import views
from django.contrib.sitemaps.views import sitemap
from products.sitemaps import ProductSitemap

sitemaps={
    'products':ProductSitemap,
}

urlpatterns = [
    path('products', views.product_list, name='product_list'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('fund-wallet', views.fundWallet, name='fund'),
]
