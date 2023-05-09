from rest_framework import serializers
from .models import Currency, Transactions

class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model =  Currency
        fields = '__all__'

class TransactionsSerializers(serializers.ModelSerializer):

    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model =  Transactions
        fields = '__all__'