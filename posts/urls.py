from django.urls import path
from .views import AddPost, Posts, PostDetail, DeletePost, EditPost, Add_Comment, Edit_Comment, Delete_Comment

urlpatterns = [
    path("", Posts.as_view(), name="posts"), 
    path("add/", AddPost.as_view(), name="add_post"),  
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("edit/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete_post"),
    path('post/<int:post_id>/add_comment/', Add_Comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', Edit_Comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', Delete_Comment, name='delete_comment'),
]
