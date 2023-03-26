from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todo.models import *


@login_required
def list_view(request):

    user_list = (request.user).userslists_set.all()
    res = []
    for obj in user_list:
        todo_list = obj.list
        list_item = ListItems.objects.select_related('list').filter(list__id=todo_list.id)
        items = []
        for item in list_item:
            items.append(item.item)

        res.append({'todo_list': todo_list, 'items': items})

    return render(request, 'list.html', {'obj': res})
