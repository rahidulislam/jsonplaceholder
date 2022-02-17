from unicodedata import name
from django.urls import path
from core.views import PostListAPIView,PostDetailAPIView
app_name = 'core'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', PostDetailAPIView.as_view(), name="post-detail")
]
