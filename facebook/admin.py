from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "location", "friends_count", "joined_on")
    search_fields = ("username", "first_name", "last_name")
