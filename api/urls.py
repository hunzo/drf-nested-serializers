from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import TransactionViewset, CurrencyViewset

router = DefaultRouter()
router.register(r'transactions', TransactionViewset)
router.register(r'currency', CurrencyViewset)

urlpatterns = router.urls

