from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return render(request, "myapp/index.html")

def products(request):
    context = {"products_list": Product.objects.all()}
    return render(request, "myapp/products.html", context)