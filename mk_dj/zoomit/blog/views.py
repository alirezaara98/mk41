from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Category, Post
from django.contrib.auth import authenticate, login
from .forms import user_reg_form, CommentForm
from django.contrib.auth.models import User

# Create your views here.

def main(request):
    return render(request, 'blog/main.html', {})
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
            'form': CommentForm(),
            'post':posts,
            'setting': posts.post_setting,
            'category': posts.category,
            'comments': posts.post_comments.filter(is_confirmed = True)
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit= False)
            comment.author = request.user
            comment.post = posts
            comment.save()

        else:
            context['form'] = form
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username = username, password = password)
        if user and user.is_active:
            login(request, user)
            return redirect('post_archive')
        else:
            pass
    return render(request, 'blog/login.html', context={})

def user_register(request):
    if request.method == 'POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['mail']
            user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            pass
        context = {'form': form}
    else:
        form = user_reg_form()
        context = {'form': form}
    return render(request, 'blog/register.html', context)
