from django.contrib import admin

# Register your models here.
from django.contrib.admin import site

from project.models import AuthorModel, BookModel

site.register(AuthorModel)
site.register(BookModel)
