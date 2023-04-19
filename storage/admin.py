from django.contrib import admin
from .models import Product, Client, AdventOrder, ConsumptionOrder, Profit

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


@admin.register(AdventOrder)
class AdventOrderAdmin(admin.ModelAdmin):
    model = AdventOrder
    list_display = ['created_at']
    list_editable=[]
    ordering = ['created_at']
    list_filter = ['created_at']
    search_fields = ['created_at']


@admin.register(ConsumptionOrder)
class ConsumptionOrderAdmin(admin.ModelAdmin):
    model = ConsumptionOrder
    list_display = ['client', 'total_cost', 'created_at']
    list_editable = []
    ordering = ['client', 'total_cost', 'created_at']
    list_filter = ['client', 'created_at']
    search_fields = ['client']


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    model = Profit
    list_display = ['client', 'profit', 'created_at']
    list_editable = []
    ordering = ['client', 'created_at', 'profit']
    list_filter = ['client', 'created_at']
    search_fields = ['client']