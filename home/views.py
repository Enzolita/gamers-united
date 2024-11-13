from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import ProfileForm
from posts.views import EditProfile
from posts.models import UserProfile, Post


class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all()[:3]



class About(TemplateView):
    template_name = 'home/about.html'

    def about(request):
        return render(request, "about.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        user_id = self.kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        profile = get_object_or_404(UserProfile, user=user)
        
       
        posts = Post.objects.filter(author=user).order_by('-created_on')  
        
        form = ProfileForm(instance=profile)
        
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['profile'] = profile
        context['form'] = form
        context['posts'] = posts
        context['post_count'] = posts.count()  # Total number of posts for the user
        return context
