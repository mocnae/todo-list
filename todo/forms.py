from django import forms
from todo.models import TodoList


class CreateForm(forms.Form):
    title = forms.CharField(max_length=100, label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, label='Описание',
        widget=forms.TextInput(attrs={'class': 'form-control'}))


