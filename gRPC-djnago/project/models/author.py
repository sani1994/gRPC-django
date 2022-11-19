"""
created at 11/13/22
"""
__author__ = "Nazmul Hasan Sani"
from django.db import models

from project.models.base import BaseModel


class AuthorModel(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = "Author's"

    def __str__(self):
        return self.name

