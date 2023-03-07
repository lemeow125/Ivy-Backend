from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import ProductSerializer, LogSerializer, UserSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-date_added')


class UserListViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LeastStockProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('quantity')

    def get_queryset(self):
        return super().get_queryset()[:1]
    # queryset = Product.objects.all().order_by('quantity').first()


class LogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = LogSerializer
    queryset = Product.history.all().order_by('-history_date')
