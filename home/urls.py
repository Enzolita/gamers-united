from django.urls import path
from .views import Index, About, ProfileView, EditProfile

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("about/", About.as_view(), name="about"), 
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="edit_profile")
]
