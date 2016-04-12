from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inventory_index_page(request):
	return HttpResponse('<html><title>Inventory list</title></html>')