from django.shortcuts import render
from .models import Product

# Create your views here.

def productpage(request):
    products = Product.objects.all()
    context = {
        "all_products": products
    }
    return render(request, "product.html", context)

def aboutpage(request):
    return render(request, 'about.html')

def singleProductView(request, id):
    single_product = Product.objects.get(id=id)
    context = {
        "product": single_product
    }
    return render(request, "product_details.html", context)

