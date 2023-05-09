from rest_framework import viewsets
from api.models import Transactions, Currency
from api.serializers import TransactionsSerializers, CurrencySerializers



class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers


class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class  = TransactionsSerializers