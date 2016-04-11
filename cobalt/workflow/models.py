from __future__ import unicode_literals

from django.db import models

from decimal import Decimal

from people.models import BaseEntity
from services.models import Service
from people.models import Employee,Customer,Contractor
# Create your models here.

STATUS_EVENTS = (
        ('Booked', 'Booked'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
		('In Progress', 'In Progress'),
		('Completed', 'Completed'),
    )
	
STATUS_BOOKING = (
        ('Booked', 'Booked'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
		('Mixing', 'Mixing'),
		('Titles', 'Titles'),
		('Completed', 'Completed'),
    )
	
PRIORITY_BOOKING = (
		('Lowes', 'Lowest'),
		('Low', 'Low'),
		('Medium', 'Medium'),
		('High', 'High'),
		('Highest', 'Highest'),
		('Critical', 'Critical'),
	)
	

class ServiceMaster(BaseEntity):
	service = models.ForeignKey('services.Service')
	assignee = models.ForeignKey('people.Employee',related_name='services_assigned',blank=True,null=True)
	contractor = models.ForeignKey('people.Contractor',related_name='services_served',blank=True,null=True)

class Event(BaseEntity):
	name = models.CharField(max_length=40)
	start_datetime = models.DateTimeField(blank=True,null=True)
	end_datetime = models.DateTimeField(blank=True,null=True)
	status = models.CharField(max_length=30, choices = STATUS_EVENTS, default='Booked')
	customer = models.ForeignKey('people.customer',related_name='events',blank=True,null=True)
	services = models.ManyToManyField('ServiceMaster',symmetrical=False)
	total = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	advance = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)
	
class Booking(BaseEntity):
	title = models.CharField(max_length=40)
	customer = models.ForeignKey('people.Customer',related_name='bookings',blank=True,null=True)
	status = models.CharField(max_length=30, choices=STATUS_BOOKING,default='Booked')
	priority = models.CharField(max_length=30, choices=PRIORITY_BOOKING,default='Low')
	expected_delivery_date = models.DateField(blank=True,null=True)
	target_date = models.DateField(blank=True,null=True)
	total = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)
	advance = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)