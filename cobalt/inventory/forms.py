from django import forms

from .models import Product


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

class NewProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name', 'company', 'price', 'total_units', 'consumed_units', 'minimum_units_to_be_maintained')
		
	def __init__(self, *args, **kwargs):
		super(NewProductForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout.append(
			FormActions(
				Submit('save', 'Submit'),
				HTML("""<a role="button" class="btn btn-default"
						href="{% url "inventory:inventory_index" %}">Cancel</a>"""),
				
		))
	