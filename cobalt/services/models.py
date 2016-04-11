from __future__ import unicode_literals

from django.db import models


from people.models import *
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=40)
	sub_category = models.ForeignKey('self', related_name='sub_categories',blank=True,null=True)
	is_active = models.BooleanField(default=True)
	
	class Meta:
		abstract = False

	def __str__(self):
		return self.name
		
class Service(models.Model):
	name = models.CharField(max_length=40)
	price = models.IntegerField()
	category = models.ForeignKey('Category',related_name='services',blank=True,null=True)
	associate = models.ForeignKey('people.Contractor',related_name='associate_services')
	resources_required = models.ManyToManyField('Equipment', symmetrical=False)
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.name
		
class Equipment(models.Model):
	name = models.CharField(max_length=40)
	cost = models.IntegerField()
	purchased_date = models.DateField(blank=True,null=True)
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.name
		
class Repair(models.Model):
	title = models.CharField(max_length=100)
	cost = models.IntegerField()
	equipment = models.ForeignKey('Equipment',related_name='repairs')
	sent_date = models.DateField(blank=True,null=True)
	received_date = models.DateField(blank=True,null=True)
	payment_date = models.DateField()
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.title
		
