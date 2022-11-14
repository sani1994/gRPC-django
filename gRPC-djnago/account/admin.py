from django.contrib import admin

# Register your models here.
from django.contrib.admin import site

from account.models import Product

site.register(Product)
