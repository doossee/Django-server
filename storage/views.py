from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Client, Advent, Consumption, Profit
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer, ClientSerializer, AdventSerializer, ConsumptionSerializer, ProfitSerializer


class ProductAPIViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class ClientAPIViewSet(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

    @action(methods=['post'], detail=False)
    def create_many(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class AdventAPIViewSet(ModelViewSet):

    queryset = Advent.objects.all()
    serializer_class = AdventSerializer
    permission_classes = [IsAdminUser]

    @action(methods=['post'], detail=False)
    def create_many(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class ConsumptionAPIViewSet(ModelViewSet):

    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    permission_classes = [IsAdminUser]

    @action(methods=['post'], detail=False)
    def create_many(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class ProfitAPIViewSet(ModelViewSet):

    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer
    permission_classes = [IsAdminUser]

    @action(methods=['post'], detail=False)
    def create_many(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


   