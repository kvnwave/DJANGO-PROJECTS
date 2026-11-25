from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """A single Facebook-style user profile shown on the cloned profile page."""

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=40, unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)
    bio = models.CharField(max_length=160, blank=True)
    location = models.CharField(max_length=120, blank=True)
    work = models.CharField(max_length=120, blank=True)
    education = models.CharField(max_length=120, blank=True)
    relationship = models.CharField(max_length=60, blank=True)
    friends_count = models.PositiveIntegerField(default=0)
    joined_on = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("first_name", "last_name")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("facebook:profile")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def initials(self):
        return "".join(
            part[:1] for part in (self.first_name, self.last_name) if part
        ).upper()


class Post(models.Model):
    """A text post written from the profile page composer."""

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.profile} — {self.content[:40]}"
