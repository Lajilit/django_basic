from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def products(request, pk=None):
    title = 'каталог товаров'
    main_product = Product.objects.all()[0]
    related_products = Product.objects.all()[1:4]
    categories = ProductCategory.objects.all()
    print(pk)

    data = {
        'title': title,
        'main_product': main_product,
        'categories': categories,
        'related_products': related_products,
    }
    return render(request, 'mainapp/products.html', context=data)
