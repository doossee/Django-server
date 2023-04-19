from rest_framework import serializers 
from .models import (
    Product,
    Client,
    Advent, AdventOrder,
    Consumption, ConsumptionOrder,
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




class AdventSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = Advent
        fields = '__all__'


class AdventGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Advent
        fields = '__all__'


class AdventOrderSerializer(serializers.ModelSerializer):
    advents = AdventSerializer(many=True)

    class Meta:
        model = AdventOrder
        fields = '__all__'
    
    def create(self, validated_data):
        advents_data = validated_data.pop('advents')
        advent_order = AdventOrder.objects.create(**validated_data)
        for advent_data in advents_data:
            advent, created = Advent.objects.get_or_create(**advent_data)
            advent_order.advents.add(advent)
        return advent_order


class AdventOrderGetSerializer(serializers.ModelSerializer):
    advents = AdventGetSerializer(many=True)

    class Meta:
        model = AdventOrder
        fields = '__all__'

    def populate_single_advent(self, single_advent_data):
        single_advent_serializer = AdventSerializer(data=single_advent_data)
        single_advent_serializer.is_valid(raise_exception=True)
        single_advent = single_advent_serializer.save()
        return single_advent

    def populate(self, validated_data):
        single_advent_data = validated_data.pop('advent')
        single_advent_list = []
        for single_advent in single_advent_data:
            single_advent_object = self.populate_single_advent(single_advent)
            single_advent_list.append(single_advent_object)
        instance = self.Meta.model(advent=single_advent_list, **validated_data)
        instance.save()
        return instance

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()




class ConsumptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = Consumption
        fields = '__all__'


class ConsumptionGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Consumption
        fields = '__all__'


class ConsumptionOrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer
    consumptions = ConsumptionSerializer(many=True)

    class Meta:
        model = ConsumptionOrder
        fields = '__all__'

    def create(self, validated_data):
        consumptions_data = validated_data.pop('consumptions')
        consumption_order = ConsumptionOrder.objects.create(**validated_data)
        for consumption_data in consumptions_data:
            consumption, created = Consumption.objects.get_or_create(**consumption_data)
            consumption_order.consumptions.add(consumption)
        return consumption_order


class ConsumptionOrderGetSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    consumptions = ConsumptionGetSerializer(many=True)

    class Meta:
        model = ConsumptionOrder
        fields = '__all__'

    def populate_single_consumption(self, single_consumption_data):
        single_consumption_serializer = ConsumptionSerializer(data=single_consumption_data)
        single_consumption_serializer.is_valid(raise_exception=True)
        single_consumption = single_consumption_serializer.save()
        return single_consumption

    def populate_client(self, client_data):
        client_serializer = ClientSerializer(data=client_data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()
        return client

    def populate(self, validated_data):
        client_data = validated_data.pop('client')
        client = self.populate_client(client_data)

        single_consumption_data = validated_data.pop('consumption')
        single_consumption_list = []
        for single_consumption in single_consumption_data:
            single_consumption_object = self.populate_single_consumption(single_consumption)
            single_consumption_list.append(single_consumption_object)
        instance = self.Meta.model(client=client, consumption=single_consumption_list, **validated_data)
        instance.save()
        return instance

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return self.populate(validated_data)
    



class ProfitSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer
    class Meta:
        model = Profit
        fields = '__all__'
    

class ProfitGetSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    class Meta:
        model = Profit
        fields = '__all__'
    
    def populate_client(self, client_data):
        client_serializer = ClientSerializer(data=client_data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()
        return client

    def populate(self, validated_data):
        client_data = validated_data.pop('client')
        client = self.populate_client(client_data)
        instance = self.Meta.model(client=client, **validated_data)
        instance.save()
        return instance

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return self.populate(validated_data)

