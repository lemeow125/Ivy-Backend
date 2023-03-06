from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    quantity = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'date_added')
        read_only_fields = ('id', 'date_added')
