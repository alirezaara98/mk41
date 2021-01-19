from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


STATUS_CHOICE = [('d', 'draft'), ('p', 'published')]


class Category(models.Model):
    title = models.CharField(_("Title"), max_length = 200)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    Parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True, related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    content = models.TextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True, null=True, blank=True)
    draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    image = models.ImageField(_("Image"), upload_to="post/images")
    category = models.ForeignKey(Category, verbose_name="category", related_name="posts",related_query_name="posts", on_delete= models.SET_NULL, null= True, blank= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("Author"),related_name='posts', related_query_name='posts',on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class PostSetting(models.Model):
    post = models.OneToOneField(Post,related_name= 'post_setting', related_query_name= 'post_setting', verbose_name=_("Post"), on_delete=models.CASCADE)
    comment = models.BooleanField(_("comment"))
    author = models.BooleanField(_("author"))
    allow_discussion = models.BooleanField(_("allow discussion"))

    class Meta:
        verbose_name = _("PostSetting")
        verbose_name_plural = _("PostSettings")


class CommentLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("author"), on_delete=models.CASCADE)
    comment = models.ForeignKey("blog.Comment", verbose_name=_("comment"), related_name= "comment_like", related_query_name="comment_like",on_delete=models.CASCADE)
    status = models.BooleanField(_("Status"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")
        unique_together = [['author', 'comment']]

    def __str__(self):
        return str(self.status)

        
class Comment(models.Model):
    content = models.TextField(_("Content"))
    post = models.ForeignKey(Post, verbose_name = _("Post"),related_name="post_comments", related_query_name="post_comments", on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']
    
    def __str__(self):
        return self.content

    @property
    def like_count(self):
        q = CommentLike.objects.filter(comment = self, status = True)
        return q.count()

    @property
    def dislike_count(self):
        q = self.comment_like.filter(comment = self,status = False)
        return q.count()


