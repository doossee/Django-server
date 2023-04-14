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

    products = ProductSerializer
    class Meta:
        model = Advent
        fields = '__all__'
    
    def create(self, validated_data):

        validated_data.pop('problem_field', None)
        instance = Advent.objects.create(**validated_data)
        instance.products.balance += instance.amount
        instance.products.save()
        return instance


class ConsumptionSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    products = ProductSerializer()
    class Meta:
        model = Consumption
        fields = '__all__'
    
    def create(self, validated_data):
        
        validated_data.pop('problem_field', None)
        instance = Consumption.objects.create(**validated_data)
        if instance.products.balance >= instance.amount > 0:
            instance.sum = instance.price * instance.amount
            instance.products.balance -= instance.amount
            instance.products.save()
            instance.client.debt += instance.sum
            instance.client.save()
        return instance


class ProfitSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    class Meta:
        model = Profit
        fields = '__all__'

    def create(self, validated_data):
        
        validated_data.pop('problem_field', None)
        instance = Profit.objects.create(**validated_data)
        instance.client.debt -= instance.sum_of_profit 
        instance.client.save()
        return instance

