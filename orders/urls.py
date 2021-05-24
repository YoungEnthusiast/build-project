from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order_create, name='order_create'),
    path('visitor-order', views.order_visitor, name='order_visitor'),
    path('st---only2', views.addOrder, name='add_order'),
]
