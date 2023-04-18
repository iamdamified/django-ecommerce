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
