from django.contrib import admin
from django.db import models
from .models import Pizzas, Toppings, Orders

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("content",)

admin.site.register(Pizzas)
admin.site.register(Toppings)
admin.site.register(Orders, OrderAdmin)