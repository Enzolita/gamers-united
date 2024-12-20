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
                attrs={"class": "form-control",
                       "placeholder": "Max 50 characters"}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or not title.strip():
            raise ValidationError
            ("Title cannot be empty or contain only spaces.")
        if len(title) > 50:
            raise ValidationError("Title cannot be longer than 50 characters.")
        return title

    def clean_category(self):
        category = self.cleaned_data.get("category")
        if not category:
            raise ValidationError("Category is required.")
        return category

    def clean_device(self):
        device = self.cleaned_data.get("device")
        if not device:
            raise ValidationError("Device is required.")
        return device

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or not content.strip():
            raise ValidationError
            ("Content cannot be empty or contain only spaces.")
        return content


class CommentForm(forms.ModelForm):
    """
    Comment form in blog posts
    """

    class Meta:
        model = Comment
        fields = ("body",)

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if not body or not body.strip():
            raise ValidationError
        ("Comment body cannot be empty or contain only spaces.")
        return body


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
            "profile_picture": forms.FileInput(),

        }
