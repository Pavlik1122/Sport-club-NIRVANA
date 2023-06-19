from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import settings
from mainapp.forms import MailForm
from mainapp.models import Products, Abonements, Favorite


def index(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            messages = f'Абонемент {form.name} \nФИ: {form.full_name} ({form.email})\nТелефон: {form.tel}'
            res = send_mail(settings.EMAIL_TITLE, messages, settings.EMAIL_HOST_USER, ['pasha3232@inbox.ru'])
            if res:
                form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = MailForm()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/index.html', context)


def tovari(request):
    products = Products.objects.all()
    context = {
        'title': 'Каталог',
        'products': products,
    }
    return render(request, 'mainapp/tovari.html', context)


def catalog(request):
    products = Products.objects.filter(counts__gt=0)
    context = {
        'title': 'Каталог',
        'products': products,

    }
    return render(request, 'mainapp/tovari.html', context)


def abonements(request):
    abonements = Abonements.objects.all()
    context = {
        'title': 'Абонементы',
        'abonements': abonements,
    }
    return render(request, 'mainapp/abonements.html', context)


def favorite(request):
    favor = Favorite.objects.filter(user=request.user)
    context = {
        'title': 'избранное',
        'favorite': favor,
    }
    return render(request, 'mainapp/favorite.html', context)


def add_favorite(request, pk):
    news = get_object_or_404(Products, id=pk)

    Favorite.objects.get_or_create(
        news=news,
        user=request.user
    )
    return HttpResponseRedirect(reverse('mainapp:index'))


def remove_favorite(request, pk):
    favor = get_object_or_404(Favorite, id=pk)
    favor.delete()
    return HttpResponseRedirect(reverse('mainapp:favorite'))


