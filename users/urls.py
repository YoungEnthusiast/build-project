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
path('dashboard/cement/update/<int:id>/', views.updateCementOrder, name='cement_update'),
path('dashboard/cement/delete/<int:id>/', views.deleteCementOrder),
path('cementorders/<str:pk>/', views.showCementOrder, name='show_cement'),
path('dashboard/select/<int:id>/', views.selectCementOrder, name='select_cement'),
path('dashboard/deselect/<int:id>/', views.deSelectCementOrder, name='deselect_cement'),
path('dashboard/checkout-many/', views.showCementOrder2, name='show_cement2'),
path('cementorders/<str:pk>/pay', views.updateWallet),
path('dashboard/checkout-many/pay/', views.updateWallet2),
path('products/cement/guest-pay/', views.guestPay, name='guest_pay'),
]
