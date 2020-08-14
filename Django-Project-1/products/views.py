from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# mapping URL /products -> index
# Uniform Resource Locator (Address)
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def prod(request):
    return HttpResponse('<h2>New Products</h2>')

