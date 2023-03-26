from django.contrib import admin
from django.urls import path
from todo.views import list_view

app_name = 'todo'

urlpatterns = [
    path('list/', list_view, name='list'),
]