from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutme',views.aboutme, name='bocharovadaria'),
    path('edupr', views.edupr, name='educationalprogram'),
    path('menegerr', views.menegerr, name='manager'),
    path('classmate', views.classmate, name='groupmates')
    ]
