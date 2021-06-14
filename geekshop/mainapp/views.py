import random
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from .models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_random_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(prod):
    same_products = Product.objects.filter(category=prod.category). \
                        exclude(pk=prod.pk)[:3]
    return same_products


def products_list(request, pk):

    if pk == 0:
        category = {'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category__pk=pk)

    content = {
        'title': 'продукты',
        'links_menu': ProductCategory.objects.all(),
        'category': category,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/products_list.html', content)


def hot_product(request):
    hot_product = get_random_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': 'горячее предложение',
        'links_menu': ProductCategory.objects.all(),
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/hot_product.html', content)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = product.name

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': product,
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


