"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"

from django_grpc_framework import generics

from project.models.author import AuthorModel
from project.serializers.author_serializer import AuthorSerializer


class AuthorService(generics.ModelService):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
