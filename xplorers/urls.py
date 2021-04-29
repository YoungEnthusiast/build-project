from django.urls import path
from xplorers import views

urlpatterns = [
path('xplore', views.showXplore, name='xplore'),
]
