from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path(r'login', views.log_in, name='log_in'),
    path(r'logout', views.log_out, name='log_out'),
    path(r'register', views.Register.as_view(), name='register'),
    path(r'', views.auth, name='auth'),
]

