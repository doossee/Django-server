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
    product = ProductSerializer()

    class Meta:
        model = SingleAdvent
        fields = '__all__'


class AdventListSerializer(serializers.ModelSerializer):
    advent = SingleAdventSerializer(many=True)

    class Meta:
        model = AdventList
        fields = '__all__'


class AdventListGetSerializer(serializers.ModelSerializer):
    advent = SingleAdventSerializer(many=True)

    class Meta:
        model = AdventList
        fields = '__all__'

    def populate_single_advent(self, single_advent_data):
        single_advent_serializer = SingleAdventSerializer(data=single_advent_data)
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


class SingleConsumptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SingleConsumption
        fields = '__all__'


class ConsumptionListSerializer(serializers.ModelSerializer):
    client = ClientSerializer
    consumption = SingleConsumptionSerializer(many=True)

    class Meta:
        model = ConsumptionList
        fields = '__all__'


class ConsumptionListGetSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    consumption = SingleConsumptionSerializer(many=True)

    class Meta:
        model = ConsumptionList
        fields = '__all__'

    def populate_single_consumption(self, single_consumption_data):
        single_consumption_serializer = SingleConsumptionSerializer(data=single_consumption_data)
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

