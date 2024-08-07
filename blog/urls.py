# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<uuid:id>/', views.detail, name='detail'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/update/<uuid:id>/', views.update_blog, name='update_blog'),
    path('blog/delete/<uuid:id>/', views.delete_blog, name='delete_blog'),
    path('blog/favorite/<uuid:id>/', views.add_to_favorites, name='add_to_favorites'),
]
