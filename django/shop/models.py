from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):
    title = models.CharField(_("Title"), max_length = 100)
    slug = models.SlugField(_("Slug"), unique= True, db_index= True)
    parent = models.ForeignKey('self', verbose_name=_("parent"), on_delete=models.SET_NULL, related_name="child", related_query_name="child", null= True, blank= True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(_("Name"), max_length= 150)
    slug = models.SlugField(_("Slug"), unique= True, db_index= True)
    description = models.TextField(_("Description"), max_length= 2000)
    image = models.ImageField(_("Image"), upload_to = "product/images")
    price = models.PositiveIntegerField(_("Price"))
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete= models.CASCADE, related_name='products', related_query_name='products')

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class ProductLike(models.Model):
    product = models.ForeignKey("shop.Product", verbose_name= _("product"), on_delete= models.CASCADE, related_name= "likes_of_product", related_query_name= "likes_of_product")
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="liked_product", related_query_name= "liked_product")
    status = models.BooleanField(_("status"))

    class Meta:
        verbose_name = _("Product_like")
        verbose_name_plural =_("Product_likes")
        unique_together = [['product', 'user']]

    def __str__(self):
        return str(self.status)

class Comment(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name="comments", related_query_name="comments")
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.CASCADE)
    content = models.CharField(_("Content"), max_length=200)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.content

class CommentLike(models.Model):
    comment = models.ForeignKey("shop.Comment", verbose_name= _("comment"), on_delete=models.CASCADE, related_name="likes_of_comment", related_query_name="likes_of_comment")
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.DO_NOTHING, null= True)
    status = models.BooleanField(_("status"))

    class Meta:
        verbose_name = "CommentLike"
        verbose_name_plural = "CommentLikes"

    def __str__(self):
        return str(self.status)
    
class Bill(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete= models.CASCADE)
    user = models.ForeignKey(User, verbose_name= _("User"),on_delete= models.CASCADE, related_name="bills", related_query_name="bills")
    number_of_product = models.IntegerField(_("NumberOfProduct"), max_length=500)
    address = models.CharField(_("Address"), max_length= 400)
    total_price = models.CharField (_("TotalPrice"), default= (number_of_product*product.price))

    class Meta:
        verbose_name = _("Bill")
        verbose_name_plural = _("Bills")

    def __str__(self):
        return "{}/{}".format(self.product.name, self.user.username)