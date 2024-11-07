from django.contrib import admin
from .models import Post, Comment, UserProfile, GameCategory


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "username", "email", "country")
    search_fields = ("user__username", "email", "country")


@admin.register(GameCategory)
class GameCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on", "category")
    list_filter = ("status", "created_on", "category")
    search_fields = ("title", "author__username", "category__name")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("user__username", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
