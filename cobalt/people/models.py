from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BaseEntity(models.Model):
	created_date = models.DateTimeField(auto_now_add = True)
	updated_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
	

class Person(BaseEntity):
	first_name = models.CharField(max_length=40,null=True,blank=True)
	last_name = models.CharField(max_length=40,blank=True,null=True)
	contact_number = models.CharField(max_length=10,blank=True,null=True)
	
	
	
	def __str__(self):
		return ' '.join([self.first_name, self.last_name])
class Customer(Person):
	business_name = models.CharField(max_length=40)
	slug = models.SlugField(unique_for_date='created_date')
	shop_number = models.CharField(max_length=40,blank=True)
	street_name = models.CharField(max_length=40,blank=True)
	town = models.CharField(max_length=40,blank=True)
	district = models.CharField(max_length=40,blank=True)
	state = models.CharField(max_length=40,blank=True)
	pin_code = models.CharField(max_length=6,blank=True)
	
	
	
class Contractor(Customer):
	first_tie_up_date = models.DateField(blank=True,null=True)
	
	
	
class Employee(Person):
	joining_date = models.DateTimeField(auto_now_add=True)
	total_leaves = models.IntegerField(blank=True,null=True)
	debited_leaves = models.IntegerField(blank=True,null=True)
	
	
	
class Leave(models.Model):
	employee = models.ForeignKey('Employee', related_name='leaves')
	applied_date = models.DateTimeField(auto_now_add=True)
	from_date = models.DateField()
	to_date = models.DateField()
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.employee
	

	