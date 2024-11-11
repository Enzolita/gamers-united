from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from .models import Post, UserProfile
from .forms import PostForm, ProfileForm


# Display list of posts (with search functionality)
class Posts(ListView):
    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            posts = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(device__icontains=query)
            )
        else:
            posts = self.model.objects.all()
        return posts


# View a detailed post
class PostDetail(DetailView):
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = "post"


# Add a new post
class AddPost(LoginRequiredMixin, CreateView):
    template_name = "posts/add_post.html"
    model = Post
    form_class = PostForm
    success_url = "/posts/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)


# Edit an existing post
class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit_post.html"
    model = Post
    form_class = PostForm
    success_url = "/posts/"

    def test_func(self):
        return self.request.user == self.get_object().author


# Delete a post
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/posts/"

    def test_func(self):
        return self.request.user == self.get_object().author


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    form_class = ProfileForm
    model = UserProfile

    def form_valid(self, form):
        self.success_url = f'/profile/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
