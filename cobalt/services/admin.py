from django.contrib import admin

from .models import Category, Service, Equipment, Repair
# Register your models here.

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Equipment)
admin.site.register(Repair)