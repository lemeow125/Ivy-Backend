from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'logs', views.LogViewSet)
router.register(r'lowest_stock_product', views.LeastStockProductViewSet)
router.register(r'user_list', views.UserListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
