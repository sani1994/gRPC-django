"""
created at 11/12/22
"""
__author__ = "Nazmul Hasan Sani"
from django.contrib.auth.models import User
from django_grpc_framework import generics

from account.models import Product
from account.serializers import UserProtoSerializer, ProductProtoSerializer


class UserService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer

    def Create(self, request, context):
        pass


