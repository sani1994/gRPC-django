"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"

from django_grpc_framework import proto_serializers

import project_pb2
from project.models.book import BookModel


class BookSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = BookModel
        proto_class = project_pb2.BookResponse
        fields = ['id', 'name', 'author', 'type']
