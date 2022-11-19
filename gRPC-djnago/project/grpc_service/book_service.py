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

    # def List(self, request, context):
    # """
    # method already implemented in base class (ModelServices).If you want any custom logic you can write it by
    #  uncommenting this method and write your custom logic.
    # """

    # def Create(self, request, context):
    #     """
    #     method already implemented in base class (ModelServices).If you want any custom logic you can write it by
    #      uncommenting this method and write your custom logic.
    #     """

    # def Update(self, request, context):
    #     """
    #     method already implemented in base class (ModelServices).If you want any custom logic you can write it by
    #      uncommenting this method and write your custom logic.
    #     """

    # def Destroy(self, request, context):
    #     """
    #     method already implemented in base class (ModelServices).If you want any custom logic you can write it by
    #      uncommenting this method and write your custom logic.
    #     """
