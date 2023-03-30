from django.contrib import admin
from django.urls import include, path
from users.views import login_view, register_view, logout_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]