from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("productinfo/", views.productInfo, name="Product Info")
]
