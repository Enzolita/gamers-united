from django.contrib import admin
from django.urls import path, include
from home.views import About, ProfileView
from posts.views import AddPost, PostDetail, Posts, EditPost, DeletePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('posts/', include('posts.urls')),
    path('about/', About.as_view(), name='about'),
    path('profile/user/<int:id>/', ProfileView.as_view(), name='profile'),
    path('posts/', Posts.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/add/', AddPost.as_view(), name='add_post'),
    path('posts/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('posts/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]
