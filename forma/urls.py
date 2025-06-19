from django.urls import path
from . import views

urlpatterns = [
    path('', views.forma_home, name='forma_home'),
    path('create', views.create, name ='create')
    ]

