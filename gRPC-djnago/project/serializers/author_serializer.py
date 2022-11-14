"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"

from django_grpc_framework import proto_serializers

import project_pb2
from project.models.author import AuthorModel


class AuthorSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = AuthorModel
        proto_class = project_pb2.AuthorModel
        fields = ['id', 'name', 'email', 'address']
