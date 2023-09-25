from django.urls import path
from .views import *

app_name = 'blogs'

urlpatterns = [
    path("posts/",posts,name="posts"),
    path("posts/post_detail",posts_detail,name="postdetail"),
]