"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"

from django_grpc_framework import generics

from project.models.book import BookModel
from project.serializers.book_serializer import BookSerializer


class BookService(generics.ModelService):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer