from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Product, Client, AdventList, ConsumptionList, Profit
from .serializers import (
    ProductSerializer, 
    ClientSerializer,
    AdventListSerializer, AdventListGetSerializer,
    ConsumptionListSerializer, ConsumptionListGetSerializer,
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

    queryset = AdventList.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdventListGetSerializer
        return AdventListSerializer
    

class ConsumptionListAPIViewSet(ModelViewSet):

    queryset = ConsumptionList.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ConsumptionListGetSerializer
        return ConsumptionListSerializer


class ProfitAPIViewSet(ModelViewSet):

    queryset = Profit.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfitGetSerializer
        return ProfitSerializer

