from .models import Product, Client, Advent, Consumption, Profit
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer, ClientSerializer, AdventSerializer, ConsumptionSerializer, ProfitSerializer


class ProductAPIViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer(queryset, many=True)
    permission_classes = [IsAdminUser]


class ClientAPIViewSet(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer(queryset, many=True)
    permission_classes = [IsAdminUser]


class AdventAPIViewSet(ModelViewSet):

    queryset = Advent.objects.all()
    serializer_class = AdventSerializer(queryset, many=True)
    permission_classes = [IsAdminUser]


class ConsumptionAPIViewSet(ModelViewSet):

    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer(queryset, many=True)
    permission_classes = [IsAdminUser]

class ProfitAPIViewSet(ModelViewSet):

    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer(queryset, many=True)
    permission_classes = [IsAdminUser]


   