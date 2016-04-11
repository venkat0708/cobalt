from __future__ import unicode_literals

from decimal import Decimal

from django.db import models

from people.models import BaseEntity
# Create your models here.

class Product(BaseEntity):
	name = models.CharField(max_length=40)
	company = models.CharField(max_length = 40,blank=True,null=True)
	price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)
	total_units = models.IntegerField(blank=True,null=True)
	consumed_units = models.IntegerField(blank=True,null=True)
	minimum_units_to_be_maintained = models.IntegerField(blank=True,null=True)