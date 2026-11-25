from django import forms

from .models import Post, Profile

INPUT_ATTRS = {"class": "input"}


class PostForm(forms.ModelForm):
    """Composer form for writing a text post on the profile page."""

    class Meta:
        model = Post
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 1, "class": "composer-input", "aria-label": "Write a post"}
            )
        }


class ProfileForm(forms.ModelForm):
    """Edit-profile modal form, including the profile picture upload."""

    def __init__(self, *args, **kwargs):
        # Class-level label_suffix is clobbered by BaseForm.__init__, so set it here.
        kwargs.setdefault("label_suffix", "")
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = (
            "profile_picture",
            "cover_photo",
            "first_name",
            "last_name",
            "bio",
            "location",
            "work",
            "education",
            "relationship",
        )
        widgets = {
            "profile_picture": forms.FileInput(
                attrs={"accept": "image/*", "class": "file-input"}
            ),
            "cover_photo": forms.FileInput(
                attrs={"accept": "image/*", "class": "file-input"}
            ),
            "first_name": forms.TextInput(attrs=INPUT_ATTRS),
            "last_name": forms.TextInput(attrs=INPUT_ATTRS),
            "location": forms.TextInput(attrs=INPUT_ATTRS),
            "work": forms.TextInput(attrs=INPUT_ATTRS),
            "education": forms.TextInput(attrs=INPUT_ATTRS),
            "relationship": forms.TextInput(attrs=INPUT_ATTRS),
            "bio": forms.Textarea(attrs={**INPUT_ATTRS, "rows": 2}),
        }
