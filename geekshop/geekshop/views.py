from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product
# Create your views here.
from mainapp.views import get_basket


def index(request):

    data = {
        'title': 'магазин',
        'products': Product.objects.all()[:4],
        'basket': get_basket(request.user),
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
