from django.shortcuts import render
from .models import Product


# Create your views here.
def products(request):
    return render(request, "pages/products/products.html", {"products":Product.objects.all()})

def product(request):
    return render(request, "pages/products/product.html", {"product":Product.objects.get(id=1)})
