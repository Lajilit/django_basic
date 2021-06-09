from django.shortcuts import render
from mainapp.models import Product
# Create your views here.


def index(request, pk=None):
    title = 'магазин'
    products = Product.objects.all()[:4]
    if pk == 0:
         products = Product.objects.all().order_by('price')[:4]
    elif pk == 1:
        products = Product.objects.all().order_by('name')[:4]

    data = {
        'title': title,
        'products': products,
    }
    return render(request, 'index.html', context=data)


def contact(request):
    title = 'наши контакты'
    data = {
        'title': title,
    }
    return render(request, 'contact.html', context=data)
