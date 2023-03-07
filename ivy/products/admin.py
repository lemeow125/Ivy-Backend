from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Product

# Register your models here.

admin.site.register(Product, SimpleHistoryAdmin)
