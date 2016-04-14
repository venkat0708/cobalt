from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.inventory_index_page, name='inventory_index'),
	url(r'^new/$', views.inventory_add_new_product, name='new_product'),
]