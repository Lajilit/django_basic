from django.shortcuts import render


# Create your views here.

def index(request):
    title = 'магазин'
    some_products = [
        {'href': 'index', 'img': '/img/product-1.jpg'},
        {'href': 'index', 'img': '/img/product-2.jpg'},
        {'href': 'index', 'img': '/img/product-3.jpg'},
        {'href': 'index', 'img': '/img/product-4.jpg'},
    ]
    data = {
        'title': title,
        'some_products': some_products,
    }
    return render(request, 'index.html', context=data)


def contact(request):
    title = 'наши контакты'
    data = {
        'title': title,
    }
    return render(request, 'contact.html', context=data)
