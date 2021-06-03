from django.urls import path
from . import views
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
]
