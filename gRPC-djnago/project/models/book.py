"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"
from django.db import models

from project.models.author import AuthorModel
from project.models.base import BaseModel


class BookModel(BaseModel):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField(AuthorModel)
    type = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = "Book's"

    def __str__(self):
        return self.name

