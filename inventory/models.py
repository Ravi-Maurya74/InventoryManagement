import uuid

from django.db import models

# Create your models here.

class Inventory(models.Model):
    STATUS_CHOICES = (
        ('CREATED','Created'),
        ('PROCURED','Procured'),
        ('SOLD','Sold')
    )

    sku = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    primary_status = models.CharField(choices=STATUS_CHOICES,max_length=30,default='CREATED')
    primary_location = models.CharField(max_length=100)
    vin = models.CharField(max_length=50)
    make = models.CharField(max_length=50,blank=True,null=True)
    model = models.CharField(max_length=50,blank=True,null=True)
    year = models.IntegerField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

