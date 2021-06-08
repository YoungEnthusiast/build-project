from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .views import ActivateAccount

urlpatterns = [
path('register', views.create, name='account'),
path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

#path('verify', views.verify_view, name='verify_view'),

path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
path('edit_profile', views.editProfile, name='edit_profile'),
path('change-password', views.changePassword, name='change_password'),
path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
path('activate/<uidb64>/<token>', ActivateAccount.as_view(), name='activate'),
path('dashboard', views.showDashboard, name='dashboard'),
path('orders', views.showOrders, name='orders'),
path('track-delivery', views.showTracks, name='tracks'),
path('invoices', views.showInvoices, name='invoices'),
path('orders/product/update/<int:id>', views.updateProductOrder, name='product_update'),
path('orders/product/delete/<int:id>', views.deleteProductOrder),
path('productorders/<str:pk>/', views.showProductOrder, name='show_product'),
path('track-history/<str:pk>', views.showTrack, name='show_track'),
path('invoices/<str:pk>', views.showInvoice, name='show_invoice'),
path('productorders/<str:pk>/pay', views.updateWallet),
path('products/product/guest-pay', views.guestPay, name='guest_pay'),
path('visitor-pay', views.visitorPay, name='visitor_pay'),
path('orders/wallet-history', views.showWallet, name='wallet_history'),
path('st---only', views.creditWallet, name='wallet_credit'),
path('card-payment', views.showPaymentComplete, name='payment_completed'),
]
