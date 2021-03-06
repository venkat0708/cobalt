from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .forms import NewProductForm
# Create your views here.

def inventory_index_page(request):
	products = Product.objects.all()
	return render(request, 'inventory/inventory_index.html', {'products': products})
	
def inventory_add_new_product(request):
	if request.method == 'POST':
		product_form = NewProductForm(request.POST)
		if product_form.is_valid():
			new_product = product_form.save()
			product_form = NewProductForm()
			return render (request, 'inventory/add_product.html',{'product_form': product_form})
	else:
		product_form = NewProductForm()
	return render(request, 'inventory/add_product.html',{ 'product_form': product_form})
	
def inventory_add_units(request):
	pass