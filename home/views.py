from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import ProfileForm  # Assuming you have a ProfileForm for the profile page


# Index View - Displaying the latest posts on the homepage
class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all()[:3]  # Displaying only the first 3 posts


# About View - Static about page
class About(TemplateView):
    template_name = 'home/about.html'

    def about(request):
        return render(request, "about.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        # Retrieve the user based on the ID passed in the URL
        user_id = self.kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        context = super().get_context_data(**kwargs)
        context['user'] = user
        return context