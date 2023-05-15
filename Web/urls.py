from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='homelink'),
    path('about/', about_page, name='aboutlink'),
    path('products/', products_page, name='productslink'),
    path('<int:pk>/', singleproduct_page, name='singlelink')
]