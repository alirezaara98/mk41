from django.contrib.auth import get_user_model
from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Post, Comment, Category, PostSetting

User = get_user_model()


# --------------normal serializing--------------------
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=120)
#     slug = serializers.SlugField()
#     content = serializers.CharField()
#     create_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#     publish_time = serializers.DateTimeField()
#     draft = serializers.BooleanField()
#     image = serializers.ImageField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.content = validated_data.get('content', instance.content)
#         instance.publish_time = validated_data.get('publish_time', instance.publish_time)
#         instance.draft = validated_data.get('draft', instance.draft)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSetting
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author_info = UserSerializer(source='author', read_only=True)
    post_setting = PostSettingSerializer(read_only=True)
    # comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author_detail = UserSerializer(source='author', read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


# ----------------------normal serializing-------------------------------
# class CommentSerializer2(serializers.Serializer):
#     content = serializers.CharField(max_length=100)
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#     author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     is_confirmed = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.content = validated_data.get('content', instance.content)
#         instance.is_confirmed = validated_data.get('is_confirmed', instance.is_confirmed)
#         instance.save()
#         return instance
