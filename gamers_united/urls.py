from django.contrib import admin
from django.urls import path, include
from home.views import About, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('posts/', include('posts.urls')),
    path('about/', About.as_view(), name='about'),
    path('profile/user/<int:id>/', ProfileView.as_view(), name='profile'),
]
