from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=now, editable=False)
    changed_by = models.ForeignKey(
        'auth.user', null=True, on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
