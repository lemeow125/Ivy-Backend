from rest_framework import serializers, mixins
from simple_history.models import HistoricalRecords
from .models import Product


class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values('id', 'history_date').order_by('history_date'))


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    quantity = serializers.IntegerField(required=False, default=0)
    history = HistoricalRecordField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'date_added', 'history')
        read_only_fields = ('id', 'date_added', 'history')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    history_date = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Product.history.model
        fields = ('history_id', 'name', 'quantity', 'history_date')
        read_only_fields = ('history_id', 'name', 'quantity', 'history_date')
