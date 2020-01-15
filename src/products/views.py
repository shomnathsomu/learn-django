from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

# Create for raw html form
def product_create_view(request):
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)

    context = {}

    return render (request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#     	form.save()
#     	form = ProductForm()

#     context = {
#     	'form': form
#     }

#     return render (request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }

    context = {
    	'object': obj
    }

    return render (request, "products/product_detail.html", context)
