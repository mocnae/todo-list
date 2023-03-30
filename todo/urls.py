from django.contrib import admin
from django.urls import path
from todo.views import list_view, delete_task, home_view, add_item, add_list, done_task

app_name = 'todo'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('task-edit/<int:id>', list_view, name='edit'),
    path('task-delete/<int:id>', delete_task, name='delete'),
    path('task-add/<int:id>', add_item, name='add-item'),
    path('list-add/', add_list, name='add-list'),
    path('task-done/<int:id>', done_task, name='done'),
]
