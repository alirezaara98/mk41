from django.urls import path
from .views import home, single, post_category
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="post_archive"),
    path('<slug:slug>', single, name="post_single"),
] 