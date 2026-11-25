from django.contrib import admin

from .models import Post, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "location", "friends_count", "joined_on")
    search_fields = ("username", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("profile", "content", "created_at")
    list_filter = ("profile",)
    search_fields = ("content",)
