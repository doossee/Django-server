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
            consumption.save()
            consumption_list.consumption.add(consumption)
        return consumption_list


class ProfitSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer
    class Meta:
        model = Profit
        fields = '__all__'


