from django.urls import path
from .views import home, single, post_category
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="posts_archive"),
    path('<slug:slug>', single, name="post_single"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
