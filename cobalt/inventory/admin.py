from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'company', 'price', 'total_units', 'consumed_units', 'minimum_units_to_be_maintained']

	
admin.site.register(Product, ProductAdmin)