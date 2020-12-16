from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import EmailField
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class User(AbstractBaseUser):
    # username = models.CharField(_("Username"), max_length=120, unique=True, db_index=True)
    full_name = models.CharField(_("FullName"), max_length= 200)
    email = models.EmailField(_("Email"), unique=True, db_index=True, primary_key=True)
    image = models.ImageField(_("Image"), null=True, blank=True)
    address = models.CharField(_("Address"), max_length=500)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["full_name"]


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    parent = models.ForeignKey('self', verbose_name=_("parent"), on_delete=models.SET_NULL, related_name="child",
                               related_query_name="child", null=True, blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    brand_name = models.CharField(_("Brand"), null=True, blank=True, max_length= 50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    description = models.TextField(_("Description"), max_length=2000)
    image = models.ImageField(_("Image"), upload_to="product/images")
    price = models.FloatField(_("Price"))
    off_percent = models.FloatField(_("Off"), default=0)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE,
                                 related_name='products', related_query_name='products')

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class ProductLike(models.Model):
    product = models.ForeignKey("shop.Product", verbose_name=_("product_like"), on_delete=models.CASCADE,
                                related_name="likes_of_product", related_query_name="likes_of_product")
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="liked_product",
                             related_query_name="liked_product")
    status = models.BooleanField(_("status"))

    class Meta:
        verbose_name = _("Product_like")
        verbose_name_plural = _("Product_likes")
        unique_together = [['product', 'user']]

    def __str__(self):
        return str(self.status)


class ProductSetting(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product_setting"), on_delete= models.CASCADE,
                                related_name="product_setting", related_query_name="product_setting")
    view = models.PositiveIntegerField(verbose_name=_("views"), default=0)
    sell = models.PositiveIntegerField(verbose_name=_("sells"), default=0)
    existance = models.BooleanField(verbose_name=_("existance"), default= True)


class Comment(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name="comments",
                                related_query_name="comments")
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.CASCADE)
    content = models.CharField(_("Content"), max_length=200)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.content


class CommentLike(models.Model):
    comment = models.ForeignKey("shop.Comment", verbose_name=_("comment"), on_delete=models.CASCADE,
                                related_name="likes_of_comment", related_query_name="likes_of_comment")
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.DO_NOTHING, null=True)
    status = models.BooleanField(_("status"))

    class Meta:
        verbose_name = "CommentLike"
        verbose_name_plural = "CommentLikes"

    def __str__(self):
        return str(self.status)


class Bill(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="bills",
                             related_query_name="bills")
    number_of_product = models.IntegerField(_("NumberOfProduct"))
    address = models.CharField(_("Address"), max_length=400)
    crated_at = models.DateTimeField(verbose_name=_("Date"), auto_now= True)

    def __str__(self):
        return "{}/{}".format(self.product.name, self.user.full_name)

    @property
    def total_price(self):
        return self.number_of_product * self.product.price
    
    @property
    def payment(self):
        return self.total_price - (self.total_price * self.product.off_percent/100)

class BillSetting(models.Model):
    bill = models.ForeignKey(Bill, verbose_name=_("BillSetting"),related_name= "billsetting" ,related_query_name="billsetting" ,on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name=_("bill_status"), default= False)