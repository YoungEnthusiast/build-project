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
handler400 = 'home.views.handler400'
handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
handler502 = 'home.views.handler502'

urlpatterns = [
    path('a-m-n/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('users.urls')),
    path('', include(('products.urls', 'products'), namespace='products')),
    path('cart', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include('xplorers.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
