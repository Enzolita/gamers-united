from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from .forms import PostForm, ProfileForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from .models import Comment, Post, GameCategory
from .forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin

# Display list of posts
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GameCategory.objects.all()
        return context


# View Post Detail
class PostDetail(DetailView):
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        context['form'] = CommentForm()
        return context

# Game categories
class Categories(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Post.objects.filter(category__id=category_id)
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GameCategory.objects.all()
        return context



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
class EditPost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = "posts/edit_post.html"
    model = Post
    form_class = PostForm
    success_url = "/posts/"
    success_message = "Post succesfully edited!"

    def test_func(self):
        return self.request.user == self.get_object().author


# Delete a post
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
    success_message = "Post successfully deleted!"

    def test_func(self):

        return self.request.user == self.get_object().author

    def delete(self, request, *args, **kwargs):

        post = self.get_object()

        response = super().delete(request, *args, **kwargs)
        return response

# Edit a profile
class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""
    form_class = ProfileForm
    model = UserProfile

    def form_valid(self, form):
        self.success_url = reverse("profile", kwargs={"id": self.kwargs["id"]})
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user_id=self.kwargs["id"])



@login_required
def Add_Comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Your comment was added successfully!")
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})


@login_required
def Edit_Comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment was updated successfully!")
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'posts/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def Delete_Comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Your comment was deleted successfully!")
        return redirect('post_detail', pk=post_id)
    return render(request, 'posts/delete_comment.html', {'comment': comment})
