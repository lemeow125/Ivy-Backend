from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import ProductSerializer, LogSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-date_added')


class LeastStockProductViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('quantity')

    def get_queryset(self):
        return super().get_queryset()[:1]


class LogViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = LogSerializer
    queryset = Product.history.all().order_by('-history_date')
