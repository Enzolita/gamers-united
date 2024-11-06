from django.urls import path
from .views import (
    AddPost, Posts,
    PostDetail, DeletePost,
    EditPost
)


urlpatterns = [
    path("add/", AddPost.as_view(), name="add_post"),
    path("", Posts.as_view(), name="posts"),
    path("<slug:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:pk>/", EditPost.as_view(), name="edit_post"),
]
