from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import AuthForm, RegForm


def login(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = AuthForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = RegForm()
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)
