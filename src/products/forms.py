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
