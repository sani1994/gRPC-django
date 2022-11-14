"""
created at 11/12/22
"""
__author__ = "Nazmul Hasan Sani"

from django.contrib.auth.models import User
from django_grpc_framework import proto_serializers
import account_pb2
from account.models import Product


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'groups']


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = account_pb2.Product_message
        fields = '__all__'
