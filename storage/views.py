from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Product, Client, AdventList, ConsumptionList, Profit
from .serializers import ProductSerializer, ClientSerializer, AdventListSerializer, ConsumptionListSerializer, ProfitSerializer

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
    serializer_class = AdventListSerializer
    permission_classes = [IsAdminUser]
    
    """def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()"""
        

class ConsumptionListAPIViewSet(ModelViewSet):

    queryset = ConsumptionList.objects.all()
    serializer_class = ConsumptionListSerializer
    permission_classes = [IsAdminUser]

    """def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()"""


class ProfitAPIViewSet(ModelViewSet):

    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer
    permission_classes = [IsAdminUser]

    """def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()"""