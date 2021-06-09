from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product
# Create your views here.


def index(request, pk=None):
    title = 'магазин'
    products = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk == 0:
         products = Product.objects.all().order_by('price')[:4]
    elif pk == 1:
        products = Product.objects.all().order_by('name')[:4]

    data = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'index.html', context=data)


def contact(request):
    title = 'наши контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    data = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'contact.html', context=data)
