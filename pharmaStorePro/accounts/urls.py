from django.urls import path
from . import views

urlpatterns=[
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_home', views.staff_dashboard, name='staff_dashboard'),
]

