from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"), db_index=True)
    details = models.CharField(_("detail"), max_length=200)
    image = models.ImageField(_("image"), upload_to="/category/")
    parent = models.ForeignKey('self', verbose_name=_("parent"), on_delete=models.SET_NULL, related_name="child",
                               related_query_name="child")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Brand(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"), db_index=True)
    details = models.CharField(_("detail"), max_length=200)
    image = models.ImageField(_("image"), upload_to="/brand/")


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.SET_NULL,
                                 related_name="product", related_query_name="product")
    brand = models.ForeignKey(Brand, verbose_name=_("brand"), on_delete=models.SET_NULL, related_name="product",
                              related_query_name="product")
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"), db_index=True)
    details = models.CharField(_("detail"), max_length=1500)
    image = models.ImageField(_("image"), upload_to="/product/")


class ProductMeta(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name="product_meta", related_query_name="product_meta")
    label = models.CharField(_("label"), max_length=100)
    value = models.CharField(_("value"), max_length=100)


class Comment(models.Model):
    user = models.ForeignKey("acounts.User", verbose_name=_("user"), on_delete=models.CASCADE,
                             related_name="comment", related_query_name="comment")
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name="product_comment", related_query_name="product_comment")
    text = models.TextField(_("text"))
    rate = models.SmallIntegerField(_("rate"), default=0)


class ShopProduct(models.Model):
    shop = models.ForeignKey("acounts.Shop", verbose_name=_("shop"), on_delete=models.CASCADE,
                             related_name="product_shop", related_query_name="product_shop")
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.PROTECT,
                                related_name="product_shop", related_query_name="product_shop")
    price = models.PositiveIntegerField(_("price"), default=0)
    quantity = models.PositiveSmallIntegerField(_("quantity"), default=0)


class Image(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name="product_image", related_query_name="product_image")
    image = models.ImageField(_("image"), upload_to="/product/")
