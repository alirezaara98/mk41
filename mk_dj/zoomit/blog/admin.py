from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models import Post, Category, Comment, PostSetting, CommentLike
# Register your models here.

def change_status(modeladmin, request, queryset):
    queryset.update(draft = False)
change_status.short_description = "Mark selected posts as published"

class ChildItemInline(admin.TabularInline):
    model = Category
    fields = ("title", "slug")
    extra = 1
    show_change_link = True

class PostInline(admin.TabularInline):
    model = Post
    fields = ("title",)
    extra = 0
    show_change_link = True

class Post_Setting(admin.TabularInline):
    model = PostSetting

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "Parent")
    search_fields = ("slug", "title")
    list_filter = ("Parent",)
    inlines = [ ChildItemInline, PostInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "create_at", "update_at","publish_time", "draft","category","author")
    search_fields = ("title", "slug")
    list_filter = ("category","draft","author")
    date_hierarchy = "publish_time"
    '''def allow_discussion(self, request, queryset):
        queryset.update()
    allow_discussion.short'''
    actions = [change_status]
    inlines = [Post_Setting]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "post", "create_at", "update_at", "author","is_confirmed", "like_count", "dislike_count")
    search_fields = ("post",)
    list_filter = ("is_confirmed", "author")
    date_hierarchy = "create_at"



admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike)
