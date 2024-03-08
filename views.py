from django.http import HttpResponse
from datetime import datetime
from .models import Category
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})



def main_view(request):
    return render(request, 'index.html')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def hello(request):
    return HttpResponse("Hello! It's my project")

def current_date(request):
    now = datetime.now()
    return HttpResponse("Current date and time: {}".format(now))

def goodbye(request):
    return HttpResponse("Goodbye, user!")

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.review_set.all() # Получение всех отзывов для данного продукта
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})