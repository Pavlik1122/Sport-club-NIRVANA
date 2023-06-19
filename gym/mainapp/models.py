from django.db import models

from authapp.models import User


# Create your models here.

class Taste(models.Model):
    name = models.CharField(verbose_name='Название вкуса', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вкус'
        verbose_name_plural = 'Вкусы'


class Products(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=120)
    img = models.ImageField(verbose_name='Изображение товара', upload_to='products/%Y/%m/%d')
    price = models.DecimalField(verbose_name='Цена товара', max_digits=10, decimal_places=2)
    cashback = models.DecimalField(verbose_name='Кешбек', max_digits=4, decimal_places=0, default=0)
    taste = models.ManyToManyField(Taste, verbose_name='Вкусы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Abonements(models.Model):
    name = models.CharField(verbose_name='Название абонемента', max_length=120)
    img = models.ImageField(verbose_name='Изображение абонемента', upload_to='products/%Y/%m/%d')
    description = models.CharField(verbose_name='Описание абонемента', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Favorite(models.Model):
    news = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
