from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.text import slugify
from django.dispatch import receiver
from django.urls import reverse

from django_resized import ResizedImageField


STATUS = ((0, "Draft"), (1, "Published"))


# Profile Model

class UserProfile(models.Model):
    """
    Database model for user's profile
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, default="Currently no bio", blank=True)
    username = models.CharField(max_length=15, default="User")
    first_name = models.CharField(max_length=15, default="Name")
    last_name = models.CharField(max_length=15, default="Lastname")
    email = models.EmailField(max_length=40, default="User@gamers-united.com")
    profile_picture = CloudinaryField(
        "image",
        default=(
            "https://res.cloudinary.com/dqk6ad4tr/image/upload/"
            "v1731314077/"
            "default_profile_picture_d3apgy.png"
        ),
        blank=True,
        null=True,
    )
    country = models.CharField(max_length=30, default="Digital Citizen", blank=True)

    def __str__(self):
        """
        Returns a string representation of the user's profile
        by using their username
        """
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        """
        Automatically create a profile when a User instance is created
        """
        if created:
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        """
        Save the user profile when the associated User instance is saved
        """
        instance.userprofile.save()

# Category Model

class GameCategory(models.Model):
    """
    Database model for game categories
    """

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")


# Post Model

class Post(models.Model):
    """
    Database model for posts, representing a blog post
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField(max_length=3000, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="posts/",
        blank=True,
        null=True,
    )

    DEVICE_CHOICES = (
        ("PC", "PC"),
        ("Nintendo Switch", "Nintendo Switch"),
        ("Xbox", "Xbox"),
        ("PlayStation", "PlayStation"),
    )
    device = models.CharField(max_length=20, choices=DEVICE_CHOICES, default=None)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            self.slug = f"{base_slug}-{timestamp}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index")


# Comment Model

class Comment(models.Model):
    """
    Database model for comments
    """

    body = models.TextField(max_length=300)
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body[:20]} by {self.user.username}"
