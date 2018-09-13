from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post_article, name='post'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
]
