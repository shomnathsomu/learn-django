from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	"""docstring for ProductForm"""
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]


class RawProductionForm(forms.Form):
	title       = forms.CharField(
					label='',
					widget=forms.TextInput(
							attrs={
								"placeholder": "Your Title"
							}
						)
					)
	description = forms.CharField(
					required=False,
					widget=forms.Textarea(
							attrs={
								"placeholder": "Your description",
								"class": "new-class-name two",
								"id": "my-id-for-textarea",
								"rows": 20,
								"cols": 120
							}
						)
					)
	price 		= forms.DecimalField(initial=199.99)
