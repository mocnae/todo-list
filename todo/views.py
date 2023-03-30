from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from todo.forms import CreateForm
from todo.models import *


@login_required
def list_view(request):

    user_list = (request.user).userslists_set.all()
    res = []
    for obj in user_list:
        todo_list = obj.list
        list_item = ListItems.objects.select_related(
            'list').filter(list__id=todo_list.id)
        items = []
        for item in list_item:
            items.append(item.item)

        res.append({'todo_list': todo_list, 'items': items})

    return render(request, 'list.html', {'obj': res})


def add_item(request, id):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        title = data.get('title')
        description = data.get('description')
        item = TodoItem(title=title, description=description, done=False)
        item.save()
        li = ListItems(list=TodoList.objects.get(id=id),
                       item=TodoItem.objects.latest('id'))
        li.save()
        return redirect('todo:list')
    return render(request, 'add_item.html', {'form': form})


def add_list(request):
    form = CreateForm(request.POST or None)
    user = request.user
    if form.is_valid():
        data = form.cleaned_data
        title = data.get('title')
        description = data.get('description')
        todo_lst = TodoList(title=title, description=description)
        todo_lst.save()
        user_lst = UsersLists(user=user, list=TodoList.objects.latest('id'))
        user_lst.save()
        return redirect('todo:list')
    return render(request, 'add_item.html', {'form': form})


def delete_task(request, id):
    item = get_object_or_404(TodoItem, id=id)
    context = {'obj': item}
    if request.method == 'GET':
        return render(request, 'delete_task.html', context)
    elif request.method == 'POST':
        item.delete()
        messages.success(request,  'The item has been deleted successfully.')
        return redirect('todo:list')
    

def done_task(request, id):
    item = TodoItem.objects.get(id=id)
    item.done = True
    item.save()
    return redirect('todo:list')


def hide_done(request):
    pass


def home_view(request):
    return render(request, 'base.html')
