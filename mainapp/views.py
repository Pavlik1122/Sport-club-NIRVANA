from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.models import Products, Abonements, Favorite


def index(request):
    context = {
        'title': 'Главная',
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