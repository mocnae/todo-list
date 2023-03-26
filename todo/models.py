from django.db import models
from users.models import CustomUser


class TodoItem(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', blank=True)
    title = models.TextField(max_length=255, verbose_name='title')
    description = models.TextField(max_length=255, verbose_name='description')
    done = models.BooleanField(verbose_name='done', default=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self) -> str:
        return self.title


class TodoList(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', blank=True)
    title = models.TextField(max_length=255, verbose_name='title')
    description = models.TextField(max_length=255, verbose_name='description')

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'

    def __str__(self) -> str:
        return self.title


class ListItems(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', blank=True)
    list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, to_field='id')
    item = models.ForeignKey(
        TodoItem, on_delete=models.CASCADE, to_field='id')

    class Meta:
        verbose_name = 'List Item'
        verbose_name_plural = 'List Items'
    
    def __str__(self) -> str:
        return f'List items {self.id}'


class UsersLists(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', blank=True)
    user = models.ForeignKey(
        CustomUser,on_delete=models.CASCADE)
    list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Users List'
        verbose_name_plural = 'Users Lists'

    def __str__(self) -> str:
        return f'UserLists for user {self.user.email}'
