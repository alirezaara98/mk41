from django.shortcuts import render
from django.template import context
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Category, Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    page = loader.get_template('blog/post.html')
    context = {
        'posts' : posts,
        'categories': category
    }
    return HttpResponse(page.render(context, request))

def single(request, slug):
    try:
        posts = Post.objects.select_related('post_setting', 'category').get(slug = slug)
    except Post.DoesNotExist:
        raise Http404('content doesnt exist!')
    context = {
        'post':posts,
        'setting': posts.post_setting,
        'category': posts.category,
    }
    return render(request, 'blog/content.html', context)

def post_category(request):
    categories = Category.objects.all()
    txt = ''
    for category in categories:
        link = reverse('post_archive', args=[ category.slug])
        txt += "<a href='{}'>{}</a><br>".format(link, category.title)
    result = '<html><head><title>Categories</title></head><body>{}</body></html>'.format(txt)
    return HttpResponse(result)

def category_posts(requests, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(category = category)
    txt = ''
    for post in posts:
        txt += '<h1>{}</h1><p>{}</p>'.format(post.title, post.content)
    result = '<html><head><title>Categories</title></head><body>{}</body></html>'.format(txt)
    return HttpResponse(result)

