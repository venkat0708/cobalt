from django.contrib import admin

from .models import Event,ServiceMaster, Booking
# Register your models here.

admin.site.register(Event)
admin.site.register(ServiceMaster)
admin.site.register(Booking)