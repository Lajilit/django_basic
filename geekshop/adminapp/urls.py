from django.urls import path
from . import views


app_name = 'adminapp'

urlpatterns = [
    path('users/create/', views.user_create,
         name='user_create'),
    path('users/read/', views.users,
         name='users'),
    path('users/update/<int:pk>/', views.user_update,
         name='user_update'),
    path('users/delete/<int:pk>/', views.user_delete,
         name='user_delete'),

    path('categories/create/', views.category_create,
         name='category_create'),
    path('categories/read/', views.categories,
         name='categories'),
    path('categories/update/<int:pk>/', views.category_update,
         name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete,
         name='category_delete'),

    path('products/create/category/<int:pk>/', views.product_create,
         name='product_create'),
    path('products/read/category/<int:pk>/', views.products,
         name='products'),
    path('products/read/<int:pk>/', views.product_read,
         name='product_read'),
    path('products/update/<int:pk>/', views.product_update,
         name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='product_delete'),
]
