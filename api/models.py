from django.db import models
from django.utils import timezone

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.code



class Transactions(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions")
    
