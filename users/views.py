from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, HttpResponse

from users.forms import UserLoginForm, UserRegistrationForm
User = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('todo:list')
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password1'])
        new_user.save()
        return HttpResponse('Register complete')
    return render(request, 'register.html', {'form': form})
