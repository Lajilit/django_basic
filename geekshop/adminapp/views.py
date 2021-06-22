from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin, DeleteView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, \
    ProductEditForm, ShopUserAdminRegisterForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.views.generic import ListView, CreateView, UpdateView


class UsersListView(ListView):
    model = ShopUser
    context_object_name = 'objects'
    template_name = 'adminapp/shopuser_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи'

        return context


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserAdminRegisterForm
    template_name = 'adminapp/shopuser_update.html'
    success_url = reverse_lazy('admin_panel:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'создание нового пользователя'

        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/shopuser_update.html'
    success_url = reverse_lazy('admin_panel:users')
    form_class = ShopUserAdminEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = \
            f'редактирование данных пользователя {self.object.username}'

        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/shopuser_delete.html'
    success_url = reverse_lazy('admin_panel:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'удаление пользователя'

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all().order_by(
        'is_deleted'
    )

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_panel:categories'))
    else:
        category_form = ProductCategoryEditForm()

    context = {
        'title': 'создание новой категории товаров',
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', context)


def category_update(request, pk):
    edit_cat = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, instance=edit_cat)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_panel:category_update', \
                                                args=[edit_cat.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_cat)

    context = {
        'title': 'редактирование категории товаров',
        'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', context)


def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk)

    if request.method == 'POST':
        # вместо удаления лучше сделаем неактивным
        category.is_deleted = True
        category.save()
        for product in products_list:
            product.is_deleted = True
            product.save()
        return HttpResponseRedirect(reverse('admin_panel:categories'))

    context = {
        'title': 'удаление категории',
        'cat_to_del': category,
        'products_to_delete': products_list,
    }

    return render(request, 'adminapp/category_delete.html', context)


class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        if pk == 0:
            context['category'] = {
                'name': 'все',
                'pk': pk
            }
            context['object_list'] = Product.objects.all().order_by(
                'is_deleted',
                'name'
            )
            context['title'] = 'Все товары'
        else:
            context['category'] = get_object_or_404(ProductCategory, pk=pk)
            context['object_list'] = Product.objects\
                .filter(category__pk=pk)\
                .order_by(
                'is_deleted',
                'name'
            )
            context['title'] = f'Товары категории {context["category"].name}'

        return context


def products(request, pk):
    if pk == 0:
        category = {
            'name': 'все',
            'pk': pk
        }
        products_list = Product.objects.all().order_by(
            'is_deleted',
            'name'
        )
        title = f'Все товары'
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(category__pk=pk).order_by(
            'is_deleted',
            'name'
        )
        title = f'Товары категории {category.name}'
    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/product_list.html', context)


def product_create(request, pk):
    if pk == 0:
        product_category = {
            'name': 'все',
            'pk': pk
        }
    else:
        product_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_panel:products',
                                                args=[pk]))
    else:
        if pk > 0:
            product_form = ProductEditForm(
                initial={'category': product_category})
        else:
            product_form = ProductEditForm()

    context = {
        'title': 'создание нового товара',
        'update_form': product_form,
        'category': product_category,
    }
    return render(request, 'adminapp/product_update.html', context)


def product_read(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': f'{product.name}',
        'object': product,
    }

    return render(request, 'adminapp/product_read.html', context)


def product_update(request, pk):
    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, \
                                    instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_panel:product_update',
                                                args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {'title': 'редактирование товара',
               'update_form': edit_form,
               'category': edit_product.category
               }

    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_deleted = True
        product.save()
        return HttpResponseRedirect(reverse('admin_panel:products', \
                                            args=[product.category.pk]))

    context = {
        'title': 'удаление товара',
        'product_to_delete': product
    }

    return render(request, 'adminapp/product_delete.html', context)
