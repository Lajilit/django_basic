from django.shortcuts import render


# Create your views here.

def products(request):
    title = 'каталог товаров'
    products_menu = [
        {'href': 'mainapp:products', 'name': 'все', 'class': 'all-active'},
        {'href': 'mainapp:products', 'name': 'дом', 'class':
            'house-active'},
        {'href': 'mainapp:products', 'name': 'офис', 'class':
            'office-active'},
        {'href': 'mainapp:products', 'name': 'модерн', 'class':
            'modern-active'},
        {'href': 'mainapp:products', 'name': 'классика', 'class':
            'classic-active'},
    ]
    related_products = [
        {'href': 'mainapp:products', 'img': '/img/product-11.jpg'},
        {'href': 'mainapp:products', 'img': '/img/product-21.jpg'},
        {'href': 'mainapp:products', 'img': '/img/product-31.jpg'},
    ]
    data = {
        'title': title,
        'products_menu': products_menu,
        'related_products': related_products
    }
    return render(request, 'mainapp/products.html', context=data)
