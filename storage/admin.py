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
    list_editable = []
    ordering = ['name', 'description', 'debt']
    list_filter = ['description']
    search_fields = ['name']


class AdventAdmin(admin.ModelAdmin):
    model = Advent
    list_display = ['products', 'amount', 'date_of']
    list_editable = []
    ordering = ['products','date_of']
    list_filter = ['products', 'date_of']
    search_fields = ['products']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.amount = form.cleaned_data['amount']
        obj.products = form.cleaned_data['products']
        obj.products.balance += obj.amount
        obj.products.save()
        super().save_model(request, obj, form, change) 


class ConsumptionAdmin(admin.ModelAdmin):
    model = Consumption
    list_display = ['client', 'products', 'price', 'amount', 'sum', 'date_of']
    list_editable = []
    ordering = ['client', 'date_of', 'products']
    list_filter = ['client', 'products', 'date_of']
    search_fields = ['client', 'products']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.client = form.cleaned_data['client']
        obj.products = form.cleaned_data['products']
        obj.amount = form.cleaned_data['amount']
        obj.price = form.cleaned_data['price']
        obj.sum = obj.price * obj.amount
        if obj.products.balance >= obj.amount > 0:
            obj.products.balance -= obj.amount
            obj.products.save()
            obj.client.debt += obj.sum
            obj.client.save()
        obj.save()
        super().save_model(request, obj, form, change) 


class ProfitAdmin(admin.ModelAdmin):
    model = Profit
    list_display = ['client', 'sum_of_profit', 'date_of']
    list_editable = []
    ordering = ['client', 'date_of', 'sum_of_profit']
    list_filter = ['client', 'date_of']
    search_fields = ['client']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sum_of_profit = form.cleaned_data['sum_of_profit']
        obj.client = form.cleaned_data['client']
        obj.client.debt -= obj.sum_of_profit
        obj.client.save()
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Advent, AdventAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
admin.site.register(Profit, ProfitAdmin)
