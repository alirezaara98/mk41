from django.urls import path, include
from .views import Home, PostContent, like_comment, add_comment
from account.views import UserLogout
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from .api import CategoryViewSet, PostListViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from zoomit.urls import router

router.register(r'posts', PostListViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', Home.as_view(), name="post_archive"),
    path('<slug:slug>', PostContent.as_view(), name="post_single"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('likecomment/', like_comment, name='like_comment'),
    path('addcomment/', add_comment, name='add_comment'),
    # path('api/posts/', PostListModelMix.as_view({'get': 'list'}), name="postapi"),
    # path('api/posts/<int:pk>', PostDetailModelMix.as_view({'get': 'retrieve'}), name="postdetailapi"),
    # path('api/comments/', comment_list, name="commentlistapi"),
    # path('api/comments/<int:pk>', comment_detail, name="commentdetailapi")
]
urlpatterns = format_suffix_patterns(urlpatterns)  # for format in class based api
