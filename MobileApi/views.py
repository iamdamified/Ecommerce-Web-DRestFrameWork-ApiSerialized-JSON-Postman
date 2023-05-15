from django.shortcuts import render
from Web.models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

#generic class based views
class api_home_page(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class api_singleproduct_page(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "id" #You must specify id, slug or uuid if you are not using pk in your urls because pk is the default so for this case lookup_field is necessary
