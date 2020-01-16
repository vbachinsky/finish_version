# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from dj_pizzas.models import Topping, Dough, Pizza, \
    InstancePizza, OrderedSnacks, Order, OrderPayment, \
    ClientAccount, ClientAccountPerson, Employee, ClientTransaction, Snack


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ordered pizzas',	{'fields': ['pizzas']}),
        ('Information',		{'fields': ['user', 'price']}),
    ]
    list_filter = ['date', 'user']
    search_fields = ['user']
    filter_horizontal = ['pizzas']
    list_display = ('id', 'user', 'price')
    readonly_fields = ('price', )


class ToppingAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['price', ]


class DoughAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['price', ]


class SnackAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['price', ]


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'image_img', ]
    fields = ['name', 'price', 'image', 'image_img', ]
    search_fields = ['name']
    list_filter = ['price', ]
    readonly_fields = ['image_img', ]


admin.site.register(Order, OrderAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Dough, DoughAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(InstancePizza)
admin.site.register(Snack, SnackAdmin)
admin.site.register(OrderedSnacks)
admin.site.register(OrderPayment)
admin.site.register(ClientAccount)
admin.site.register(ClientAccountPerson)
admin.site.register(Employee)
admin.site.register(ClientTransaction)
