from django.urls import path, include
from .views import Index, About



urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('summernote/', include('django_summernote.urls')),
]