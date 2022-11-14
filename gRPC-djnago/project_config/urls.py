"""project_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import project_pb2_grpc
from project.grpc_service.author_service import AuthorService
from project.grpc_service.book_service import BookService

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    project_pb2_grpc.add_AuthorModelControllerServicer_to_server(AuthorService.as_servicer(), server)
    project_pb2_grpc.add_BookControllerServicer_to_server(BookService.as_servicer(), server)
