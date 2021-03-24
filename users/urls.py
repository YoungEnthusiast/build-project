from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('register/', views.create, name='account'),
path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
path('edit_profile/', views.editProfile, name='edit_profile'),
path('change-password/', views.changePassword, name='change_password'),
path('dashboard/', views.showDashboard, name='dashboard'),
path('dashboard/product/update/<int:id>/', views.updateProductOrder, name='product_update'),
path('dashboard/product/delete/<int:id>/', views.deleteProductOrder),
path('productorders/<str:pk>/', views.showProductOrder, name='show_product'),
path('dashboard/select/<int:id>/', views.selectProductOrder, name='select_product'),
path('dashboard/deselect/<int:id>/', views.deSelectProductOrder, name='deselect_product'),
path('dashboard/checkout-many/', views.showProductOrder2, name='show_product2'),
path('productorders/<str:pk>/pay', views.updateWallet),
path('dashboard/checkout-many/pay/', views.updateWallet2),
path('products/product/guest-pay/', views.guestPay, name='guest_pay'),
]
