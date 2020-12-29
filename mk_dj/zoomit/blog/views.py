import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
# from django.template import loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Post, CommentLike, Comment
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import CommentForm
from django.views.generic import ListView, DetailView, TemplateView
from datetime import datetime

# from django.views.generic import DetailView

User = get_user_model()


# Create your views here.
class Main(TemplateView):
    template_name = 'blog/main.html'


# def main(request):
#     return render(request, 'blog/main.html', {})


# def home(request):

# posts = Post.objects.all()
# category = Category.objects.all()
# page = loader.get_template('blog/post.html')
# context = {
#     'posts': posts,
#     'categories': category
# }
# return HttpResponse(page.render(context, request))
class Home(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False, publish_time__lte=datetime.now())
    ordering = 'publish_time'
    template_name = 'blog/post.html'


class PostContent(DetailView):
    model = Post
    template_name = 'blog/content.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            post = queryset.select_related('post_setting', 'category').get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        comments = self.get_object().post_comments.filter(is_confirmed=True)
        context['post'] = self.get_object()
        context['setting'] = self.get_object().post_setting
        context['category'] = self.get_object().category
        context['comments'] = comments
        return context


# def single(request, slug):
#     try:
#         posts = Post.objects.select_related('post_setting', 'category').get(slug=slug)
#     except Post.DoesNotExist:
#         raise Http404('content doesnt exist!')
#     context = {
#         'post': posts,
#         'setting': posts.post_setting,
#         'category': posts.category,
#         'comments': posts.post_comments.filter(is_confirmed=True)
#     }
#     return render(request, 'blog/content.html', context)


# class Single(DetailView):
#     model = Post
#     http_method_names = ['get', 'post']
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'
#
#     def __init__(self, slug, **kwargs):
#         super().__init__(**kwargs)
#         self.slug = slug
#
#     def get_queryset(self=None):
#         try:
#             queryset = Post.objects.select_related('post_setting', 'category').get(slug=self.slug)
#         except Post.DoesNotExist:
#             raise Http404('content doesnt exist')
#         return queryset
#
# extra_context = {'form': CommentForm(), 'setting': get_queryset().post_setting, 'category': get_queryset(
# ).category, 'comments': get_queryset().post_comments.filter(is_confirmed=True)}


class CategoryMenu(ListView):
    # categories = Category.objects.all()
    # txt = ''
    # for category in categories:
    #     link = reverse('post_archive', args=[category.slug])
    #     txt += "<a href='{}'>{}</a><br>".format(link, category.title)
    # result = '<html><head><title>Categories</title></head><body>{}</body></html>'.format(txt)
    # return HttpResponse(result)
    model = Category
    queryset = Category.objects.all()
    template_name = 'blog/category.html'


# def category_posts(requests, slug):
# category = Category.objects.get(slug=slug)
# posts = Post.objects.filter(category=category)
# txt = ''
# for post in posts:
#     txt += '<h1>{}</h1><p>{}</p>'.format(post.title, post.content)
# result = '<html><head><title>Categories</title></head><body>{}</body></html>'.format(txt)
# return HttpResponse(result)

class CategoryPosts(DetailView):
    model = Category
    template_name = 'blog/category_posts.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        category = super().get_object()
        return category

    def get_context_data(self, *, object_list=None, **kwargs):
        # category = Category.objects.get(slug=self.slug_url_kwarg)
        posts = Post.objects.filter(category=self.get_object())
        context = super().get_context_data(**kwargs)
        context['posts'] = posts
        context['category'] = self.get_object()
        return context


# def like_comment(request, post_link):
#     if request.method == 'POST':
#         form = CommentLikeForm(request.POST)
#         if form.is_valid():
#             status = form.cleaned_data['status']
#             comment_id = form.cleaned_data['comment']
#             try:
#                 comment_like = CommentLike.objects.get(author=request.user, comment_id=comment_id)
#                 comment_like.status = status
#                 comment_like.save()
#             except:
#                 CommentLike.objects.create(autor=request.user, comment_id=comment_id, status=status)
#     else:
#         pass
#     return redirect('post_single', post_link)
@login_required
@csrf_exempt
def like_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.get(id=data['commentid'])
    except Comment.DoesNotExist:
        return HttpResponse('doesnt exist', status=404)
    try:
        comment_like = CommentLike.objects.get(author=user, comment=comment)
        comment_like.status = data['status']
        comment_like.save()
    except CommentLike.DoesNotExist:
        CommentLike.objects.create(author=user, status=data['status'], comment=comment)
    response = {'like_count': comment.like_count, 'dislike_count': comment.dislike_count}
    return HttpResponse(json.dumps(response), status=201)


@login_required
@csrf_exempt
def add_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        post = Post.objects.get(id=data['postid'])
    except Post.DoesNotExist:
        return HttpResponse("content doesn't exist", status=404)
    try:
        comment = Comment.objects.create(content=data['content'], post=post, author=user)
    except Comment.DoesNotExist:
        return HttpResponse("couldn't create comment", status=500)
    # response = {'comment': comment,}
    response = {'comment_content': comment.content, 'comment_id': comment.id,
                'comment_author': comment.author.profile_name, 'comment_like': comment.like_count,
                'comment_dislike': comment.dislike_count}
    return HttpResponse(json.dumps(response), status=201)
