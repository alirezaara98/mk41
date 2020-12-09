"""zoomit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog.views import home, single, post_category, category_posts, user_login, user_register, main
urlpatterns = [
    path('', main, name='main_page'),
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
    path('category/', post_category, name= 'category_archive'),
    path('category/<slug:slug>', category_posts, name='category_single'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)