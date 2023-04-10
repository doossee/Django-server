from rest_framework import serializers 
from .models import Product, Client, Advent, Consumption, Profit


class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = '__all__' 


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'


class AdventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advent
        fields = '__all__'


class ConsumptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Consumption
        fields = '__all__'


class ProfitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profit
        fields = '__all__'


