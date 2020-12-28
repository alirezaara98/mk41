from django.urls import path
from .views import Home, PostContent, like_comment, add_comment
from account.views import UserLogout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name="post_archive"),
    path('<slug:slug>', PostContent.as_view(), name="post_single"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('likecomment/', like_comment, name='like_comment'),
    path('addcomment/', add_comment, name='add_comment'),
]
