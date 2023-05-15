from django.urls import path
from .views import api_home_page, api_singleproduct_page

urlpatterns = [
    path('', api_home_page.as_view(), name='homelink'),
    # path('about/', about_page, name='aboutlink'),
    # path('products/', products_page, name='productslink'),
    path('<int:pk>/', api_singleproduct_page.as_view(), name='singlelink')
]