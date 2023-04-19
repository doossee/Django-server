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
    client = ClientSerializer()
    consumption = SingleConsumptionSerializer(many=True)

    class Meta:
        model = ConsumptionList
        fields = '__all__'

    def populate_client(self, client_data):
        client_serializer = ClientSerializer(data=client_data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.populate(client_serializer.validated_data)
        return client

    def populate_consumption(self, consumption_data):
        consumption_serializer = SingleConsumptionSerializer(data=consumption_data)
        consumption_serializer.is_valid(raise_exception=True)
        consumption = consumption_serializer.populate(consumption_serializer.validated_data)
        return consumption

    def populate(self, validated_data):
        client_data = validated_data.pop('client')
        consumption_data = validated_data.pop('consumption')
        client = self.populate_client(client_data)
        consumption = [self.populate_consumption(data) for data in consumption_data]
        consumption_list = ConsumptionList.objects.create(client=client, **validated_data)
        consumption_list.consumption.set(consumption)
        return consumption_list

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return self.populate(validated_data)


class ProfitSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer
    class Meta:
        model = Profit
        fields = '__all__'


