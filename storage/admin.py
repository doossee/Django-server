from django.contrib import admin
from .models import Product, Client, AdventList, ConsumptionList, Profit

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    model = Product
    list_display = ['name', 'type', 'balance']
    ordering = ['name', 'type', 'balance']
    list_filter = ['type']
    search_fields = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'description', 'phone_number', 'debt', 'status']
    ordering = ['name', 'description', 'debt']
    list_filter = ['description', 'status']
    search_fields = ['name']


@admin.register(AdventList)
class AdventListAdmin(admin.ModelAdmin):
    model = AdventList
    list_display = ['created_at']
    list_editable=[]
    ordering = ['created_at']
    list_filter = ['created_at']
    search_fields = ['created_at']

    """def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.amount = form.cleaned_data['amount']
        obj.products = form.cleaned_data['products']
        obj.products.balance += obj.amount
        obj.products.save()
        super().save_model(request, obj, form, change)"""


@admin.register(ConsumptionList)
class ConsumptionListAdmin(admin.ModelAdmin):
    model = ConsumptionList
    list_display = ['client', 'total_cost', 'created_at']
    list_editable = []
    ordering = ['client', 'total_cost', 'created_at']
    list_filter = ['client', 'created_at']
    search_fields = ['client']

    """def save_model(self, request, obj, form, change):
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
        super().save_model(request, obj, form, change)"""


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    model = Profit
    list_display = ['client', 'profit', 'created_at']
    list_editable = []
    ordering = ['client', 'created_at', 'profit']
    list_filter = ['client', 'created_at']
    search_fields = ['client']

    """def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sum_of_profit = form.cleaned_data['sum_of_profit']
        obj.client = form.cleaned_data['client']
        obj.client.debt -= obj.sum_of_profit
        obj.client.save()
        super().save_model(request, obj, form, change)"""

