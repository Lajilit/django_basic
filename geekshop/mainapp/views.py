from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

# Create your views here.


# def products(request):
#     title = 'каталог товаров'
#     main_product = Product.objects.all()[0]
#     related_products = Product.objects.all()[1:4]
#     categories = ProductCategory.objects.all()
#
#     data = {
#         'title': title,
#         'main_product': main_product,
#         'categories': categories,
#         'related_products': related_products,
#     }
#     return render(request, 'mainapp/products.html', context=data)


def products(request, pk=None):

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk == 0:
        products = Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category__pk=pk).order_by('price')

    content = {
        'title': title,
        'links_menu': links_menu,
        'category': category,
        'products': products,
    }

    return render(request, 'mainapp/products_list.html', content)


def product(request, pk=None):

    title = 'продукты'
    main_product = Product.objects.get(pk=1)
    links_menu = ProductCategory.objects.all()

    if pk:
        main_product = Product.objects.get(pk=pk)

    same_products = Product.objects.exclude(
        pk=main_product.pk).filter(category__pk=main_product.category.pk)[:3]

    content = {
        'title': title,
        'links_menu': links_menu,
        'main_product': main_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', content)



