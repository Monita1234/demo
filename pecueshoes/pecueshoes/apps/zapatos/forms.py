from django import forms
from pecueshoes.apps.zapatos.models import Zapatos
'''
class add_zapatos_form(forms.Form):
	marca		= forms.CharField(widget = forms.TextInput()) 
	color		= forms.CharField(widget = forms.Textarea())
	cantidad	= forms.CharField(widget = forms.Textarea())
	material	= forms.CharField(widget = forms.Textarea())
	precio		= forms.DecimalField(required = True)
	talla		= forms.CharField(widget = forms.Textarea())
	modelo		= forms.CharField(widget = forms.Textarea())
	importado	= forms.CharField(widget = forms.Textarea())

	def clean (self):
		return self.cleaned_data

'''


class add_zapatos_form(forms.ModelForm):
	class Meta:
		model = Zapatos
