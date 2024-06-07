from django.urls import path,include
from rest_framework.routers import DefaultRouter
from store.api.views import ProductViewset

router=DefaultRouter()
router.register('product',ProductViewset,basename='product')
urlpatterns = [
    path('', include(router.urls)),
]