from django.db import models
from purchaser.models import Purchaser
from django.utils import timezone
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=100,decimal_places=2)
    def __str__(self):
        return self.name + " ( $"+self.unit_price+")" 
class Transaction_Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Transaction(models.Model):
    buyer = models.ForeignKey(Purchaser,on_delete = models.CASCADE)
    transaction_type = models.ForeignKey(Transaction_Type,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.created_date)
    def total(self):
        total = 0
        reds =self.transaction_red_set.all()
        for red in reds:
            total += red.total()
        greens = self.transaction_green_set.all()
        for green in greens:
            total -= green.amount 
        return total
class Transaction_Red(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    qty = models.IntegerField()
    def __str__(self):
        return self.item.name
    def total(self):
        item = Item.objects.get(pk = self.item_id)
        total = item.unit_price * self.qty
        return total
class Transaction_Green(models.Model):
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    transaction = models.ForeignKey(Transaction,on_delete = models.CASCADE)
    def __str__(self):
        return self.amount


