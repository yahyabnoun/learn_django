from django.shortcuts import render
from .models import Product


# Create your views here.
def products(request):
    objectproducts = Product.objects
    # products = {"products":objectproducts.filter(name__contains="x")}
    products = {"products":objectproducts.filter(name__contains="x")}
    return render(request, "pages/products/products.html", products)

def product(request):
    return render(request, "pages/products/product.html", {"product":Product.objects.get(id=1)})
