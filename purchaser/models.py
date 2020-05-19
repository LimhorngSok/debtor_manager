from django.db import models
from django.utils import timezone
# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        unique_together = (('name'),)
class Purchaser(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name
    def totalDept(self):
        total = 0
        transactions = self.transaction_set.all()
        for transaction in transactions:
            total += transaction.total()
        return total
