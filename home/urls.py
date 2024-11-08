from django.urls import path
from .views import Index, About, ProfileView

urlpatterns = [
    path("", Index.as_view(), name="home"),  # Home page
    path("about/", About.as_view(), name="about"),  # About page
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),  # User's profile with ID
]
