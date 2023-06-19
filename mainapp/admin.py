from django.contrib import admin

# Register your models here.
from mainapp.models import Products, Taste, Abonements, Favorite, Feedback

admin.site.register(Products)
admin.site.register(Taste)
admin.site.register(Abonements)
admin.site.register(Favorite)
admin.site.register(Feedback)