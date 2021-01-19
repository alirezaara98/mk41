from django.shortcuts import render, redirect
from .models import Product, Category
from django.views.generic.detail import BaseDetailView


# Create your views here.
class CategoryDetail(BaseDetailView):
    model = Category
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
