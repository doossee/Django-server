from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Product, Client, AdventOrder, ConsumptionOrder, Profit
from .serializers import (
    ProductSerializer, 
    ClientSerializer,
    AdventOrderSerializer, AdventOrderGetSerializer,
    ConsumptionOrderSerializer, ConsumptionOrderGetSerializer,
    ProfitSerializer, ProfitGetSerializer
)
class ProductAPIViewSet(ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ClientAPIViewSet(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]


class AdventListAPIViewSet(ModelViewSet):

    queryset = AdventOrder.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if not self.request.method == "GET":
            return AdventOrderSerializer
        return AdventOrderGetSerializer
    

class ConsumptionListAPIViewSet(ModelViewSet):

    queryset = ConsumptionOrder.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if not self.request.method == "GET":
            return ConsumptionOrderSerializer
        return ConsumptionOrderGetSerializer


class ProfitAPIViewSet(ModelViewSet):

    queryset = Profit.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if not self.request.method == "GET":
            return ProfitSerializer
        return ProfitGetSerializer

