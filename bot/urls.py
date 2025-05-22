# bot/urls.py
from django.urls import path
from .views import register_user, get_user_info

urlpatterns = [
    path('register', register_user),
    path('user/<int:user_id>', get_user_info),
]