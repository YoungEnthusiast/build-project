"""build URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('a-m-n/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('users.urls')),
    path('products/', include('cement.urls')),


    # path('about-buildqwik/', views.showAbout, name='about'),
    # path('contact-us/', views.showContact, name='contact'),
    # path('st---only/', views.showContacts, name='contacts'),
    #path('products/cement/', views.showCement, name='cement'),

    # users app urls starts here
    # path('register/', users_views.create, name='account'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('edit_profile/', users_views.editProfile, name='edit_profile'),
    # path('change-password/', users_views.changePassword, name='change_password'),
    # path('dashboard/', users_views.showDashboard, name='dashboard'),
    #
    # # store app urls starts here
    # path('cement/', store_views.showCement, name='cement'),
    # path('products/cement/', store_views.showStore, name='store'),
    # path('cart/', store_views.showCart, name='cart'),
    # path('checkout/', store_views.showCheckOut, name='checkout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
