from django.contrib import admin
from .models import TodoItem, TodoList, ListItems, UsersLists

admin.site.register(TodoItem)
admin.site.register(TodoList)
admin.site.register(ListItems)
admin.site.register(UsersLists)
