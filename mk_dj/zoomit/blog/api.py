from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .models import Post, Comment, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


class PostListViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk):
        post = self.get_object()
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_published(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(draft=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def publish(self, request, pk):
        post = self.get_object()
        post.draft = False
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(is_confirmed=True)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
# --------------generic api view----------------
# class PostListGenMix(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#
# class PostDetailGenMix(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# --------------------Mixin api view--------------------------
# class PostListMix(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetailMix(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
# generics.GenericAPIView): serializer_class = PostSerializer queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# ------------------------class based api view-------------------------
# class PostList(APIView):
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, deta=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------function based api view----------------------
# @csrf_exempt
# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @csrf_exempt
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(id=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def comment_list(request):
#     if request.method == 'GET':
#         comments = Comment.objects.filter(is_confirmed=True)
#         serializer = CommentSerializer(comments, many=True)
#         print(serializer)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CommentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def comment_detail(request, pk):
#     try:
#         comment = Comment.objects.get(id=pk)
#     except Comment.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CommentSerializer(comment, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         comment.delete()
#         return HttpResponse(status=204)
