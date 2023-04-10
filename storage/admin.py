from django.contrib import admin
from .models import Product, Client, Advent, Consumption, Profit


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'type', 'balance']
    ordering = ['name', 'type', 'balance']
    list_filter = ['type']
    search_fields = ['name']


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'description', 'debt']
    ordering = ['name', 'description', 'debt']
    list_filter = ['description']
    search_fields = ['name']


class AdventAdmin(admin.ModelAdmin):
    model = Advent
    list_display = ['product', 'amount', 'date_of']
    ordering = ['product','date_of']
    list_filter = ['product', 'date_of']
    search_fields = ['product']


class ConsumptionAdmin(admin.ModelAdmin):
    model = Consumption
    list_display = ['client', 'product', 'price', 'amount', 'sum', 'date_of']
    ordering = ['client', 'date_of', 'product']
    list_filter = ['client', 'product', 'date_of']
    search_fields = ['client', 'product']


class ProfitAdmin(admin.ModelAdmin):
    model = Profit
    list_display = ['client', 'sum_of_profit', 'date_of']
    ordering = ['client', 'date_of', 'sum_of_profit']
    list_filter = ['client', 'date_of']
    search_fields = ['client']

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Advent, AdventAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
admin.site.register(Profit, ProfitAdmin)
