from django.urls import path
from .views import CategoryDetail

urlpatterns = [path('category/<slug:pk>', CategoryDetail.as_view(), name="category_detail"), ]
