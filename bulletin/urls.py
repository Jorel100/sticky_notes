# bulletin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.bulletin_post_list, name='bulletin_post_list'),
    path('posts/<int:pk>/', views.bulletin_post_detail, name='bulletin_post_detail'),
    path('posts/new/', views.bulletin_post_new, name='bulletin_post_new'),
    path('posts/<int:pk>/edit/', views.bulletin_post_edit, name='bulletin_post_edit'),
]
