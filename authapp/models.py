from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=150, )
    last_name = models.CharField(verbose_name='Фамилия', max_length=150, )
    patronymic = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.username
