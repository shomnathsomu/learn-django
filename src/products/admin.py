from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)


# create python object in the python shell
# python manage.py shell
# from products.models import Product
# Product.objects.create(title='Mercedes-Benz', description='Origin: Germany', price='$2M USD', summary='Looking pretty')
