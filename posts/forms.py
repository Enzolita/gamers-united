from django import forms
from djrichtextfield.widgets import RichTextWidget
from django.contrib.auth.models import User

from django_summernote.widgets import SummernoteWidget

from .models import Post, Comment, UserProfile, GameCategory
from django.contrib.auth.mixins import LoginRequiredMixin


class PostForm(forms.ModelForm):
    """
    PostForm for blog posting
    """

    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "device",
            "content",
            "image",
        ]
        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "device": forms.Select(attrs={"class": "form-control"}),
            "content": SummernoteWidget(attrs={"class": "form-control"}),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Max 50 characters"}
            ),
        }


class CommentForm(forms.ModelForm):
    """
    Comment form in blog posts
    """

    class Meta:
        model = Comment
        fields = ("body",)

    body = forms.CharField(max_length=300)


class UserForm(forms.ModelForm):
    """
    Form for user registration and profile information
    """

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)


class ProfileForm(forms.ModelForm):
    """
    User profile page form
    """

    class Meta:
        model = UserProfile
        fields = [
            "bio",
            "profile_picture",
            "country",
        ]
        widgets = {
            "profile_picture": forms.FileInput(),  # forms.FileInput for
            # custom rendering, removing current url link displayed
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=55)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
