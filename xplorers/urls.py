from django.urls import path
from xplorers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#path('xplore/register/', views.create, name='explore_account'),
# path('xplore/login/', auth_views.LoginView.as_view(template_name='explore_xplorers/login.html'), name='explore_login'),
# path('xplore/logout/', auth_views.LogoutView.as_view(template_name='explore_xplorers/logout.html'), name='explore_logout'),
#path('xplore/edit_profile/', views.editProfile, name='explore_edit_profile'),
# path('xplore/change-password/', views.changePassword, name='explore_change_password'),
# path('xplore/reset-password/', auth_views.PasswordResetView.as_view(template_name='explore_xplorers/reset_password.html'), name='explore_reset_password'),
# path('xplore/reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='explore_xplorers/password_reset_sent.html'), name='explore_password_reset_done'),
# path('xplore/reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='explore_xplorers/password_reset_form.html'), name='explore_password_reset_confirm'),
# path('xplore/reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='explore_xplorers/password_reset_done.html'), name='explore_password_reset_complete'),

# path('xplore/dashboard/', views.showDashboard, name='explore_dashboard'),
# path('xplore/orders/', views.showOrders, name='explore_orders'),
# path('xplore/invoices/', views.showInvoices, name='explore_invoices'),
# path('xplore/orders/product/update/<int:id>/', views.updateProductOrder, name='explore_product_update'),
# path('xplore/orders/product/delete/<int:id>/', views.deleteProductOrder),
# path('xplore/productorders/<str:pk>/', views.showProductOrder, name='explore_show_product'),
# path('xplore/orders/select/<int:id>/', views.selectProductOrder, name='explore_select_product'),
# path('xplore/orders/deselect/<int:id>/', views.deSelectProductOrder, name='explore_deselect_product'),
# path('xplore/invoices/select/<int:id>/', views.selectInvoice, name='explore_select_invoice'),
# path('xplore/invoices/deselect/<int:id>/', views.deSelectInvoice, name='explore_deselect_invoice'),
# path('xplore/invoices/<str:pk>/', views.showInvoice, name='explore_show_invoice'),
# path('xplore/orders/checkout-many/', views.showProductOrder2, name='explore_show_product2'),
# path('xplore/invoices/view/many/', views.showInvoiceMany, name='explore_show_invoices'),
# path('xplore/productorders/<str:pk>/pay', views.updateWallet),
# path('xplore/orders/checkout-many/pay/', views.updateWallet2),
# path('xplore/products/product/guest-pay/', views.guestPay, name='explore_guest_pay'),
# path('xplore/orders/wallet-history/', views.showWallet, name='explore_wallet_history'),
]
