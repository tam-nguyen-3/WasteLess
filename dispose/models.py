from django.db import models
from django.utils import timezone

# Create your models here.
class MenuItem(models.Model):
    itemName = models.CharField(max_length=200)
    unitPrice = models.FloatField("Unit price")
    unitWeight = models.FloatField("Unit weight (oz)")

    def __str__(self):
        return self.itemName

class Dispose(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    disposeDate = models.DateField("Disposal date")
    numItem = models.IntegerField()

    def __str__(self):
        return self.item.itemName