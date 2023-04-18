from rest_framework import serializers 
from .models import (
    Product,
    Client,
    SingleAdvent,
    AdventList,
    SingleConsumption,
    ConsumptionList,
    Profit
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SingleAdventSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = SingleAdvent
        fields = '__all__'

class AdventListSerializer(serializers.ModelSerializer):
    advent = SingleAdventSerializer(many=True)

    class Meta:
        model = AdventList
        fields = '__all__'

    def create(self, validated_data):
        advents_data = validated_data.pop('advent')
        advent_list = AdventList.objects.create(**validated_data)
        for advent_data in advents_data:
            advent, created = SingleAdvent.objects.get_or_create(**advent_data)
            advent_list.advent.add(advent)
        return advent_list


class SingleConsumptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = SingleConsumption
        fields = '__all__'

class ConsumptionListSerializer(serializers.ModelSerializer):
    client = ClientSerializer
    consumption = SingleConsumptionSerializer(many=True)
    
    class Meta:
        model = ConsumptionList
        fields = '__all__'

    def create(self, validated_data):
        consumptions_data = validated_data.pop('consumption')
        consumption_list = ConsumptionList.objects.create(**validated_data)
        for consumption_data in consumptions_data:
            consumption, created = SingleConsumption.objects.get_or_create(**consumption_data)
            consumption_list.consumption.add(consumption)
        return consumption_list
    


"""
  
    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            order.products.add(product)
        return order

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.products.clear()
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            instance.products.add(product)
        instance.save()
        return instanceproduct = ProductSerializer
    amount = serializers.IntegerField(min_value=0)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, min_value=0)
    sum = serializers.SerializerMethodField()

    def get_sum(self, obj):
        return obj.amount * obj.price"""



class ProfitSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer
    class Meta:
        model = Profit
        fields = '__all__'


