from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('category/<int:pk>/', views.products, name='index'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<int:pk>/', views.products, name='category'),
]
