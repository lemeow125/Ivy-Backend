from django.db import models
from django.utils.timezone import now
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
