from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SlideShow
from products.models import Category, Product


# Create your views here.

class MainPage(TemplateView):
    template_name = 'main/index.html'
    extra_context = {'slides': SlideShow.objects.all(), 'categories': Category.objects.filter(~Q(name='clothes')),
                     'products': Product.objects.annotate(id_count=Count('id')).order_by('-id')[:4]}
