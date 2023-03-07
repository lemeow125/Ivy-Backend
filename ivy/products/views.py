from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ProductSerializer, LogSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class LogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = LogSerializer
    queryset = Product.history.all().order_by('-history_date')
