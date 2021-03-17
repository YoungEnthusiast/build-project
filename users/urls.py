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
path('dashboard/cement/delete/<int:pk>/', views.CementOrderDeleteView.as_view()),
path('cementorders/<str:pk>/', views.showCementOrder, name='show_cement'),
]
