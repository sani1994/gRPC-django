"""
created at 11/12/22
"""
__author__ = "Nazmul Hasan Sani"

from django.contrib.auth.models import User
from django_grpc_framework import generics

from account.models import Product
from account.serializers import ProductProtoSerializer


class ProductService(generics.ModelService):
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer
