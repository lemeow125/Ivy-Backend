from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('logs/', views.LogViewSet.as_view()),
    path('lowest_stock_product/', views.LeastStockProductViewSet.as_view())
]
