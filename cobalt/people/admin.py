from django.contrib import admin
from django import forms
from .models import Customer, Employee, Contractor,Leave


# Register your models here.
class LeaveForm(forms.ModelForm):
	class Meta:
		model  = Leave
		fields = ('employee','from_date','to_date')
		
	def clean(self):
		data = self.cleaned_data
		try:
			employee = data['employee']
			start = data['from_date']
			end = data['to_date']
		except KeyError:
			raise forms.ValidationError("")
		num = (end-start).days
		if num > employee.total_leaves - employee.debited_leaves:
			raise forms.ValidationError("%s does not have %s number of leaves available"%(employee,num))

class LeaveAdmin(admin.ModelAdmin):
	
	form = LeaveForm
	
	def save_model(self, request, obj, form, change):
		num_of_days = (obj.to_date - obj.from_date).days
		emp = obj.employee
		emp.debited_leaves = emp.debited_leaves
		emp.save()
		obj.save()

		




admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Contractor)
admin.site.register(Leave, LeaveAdmin)
