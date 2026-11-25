from django import forms

from .models import Profile

INPUT_ATTRS = {"class": "input"}


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
            "first_name": forms.TextInput(attrs=INPUT_ATTRS),
            "last_name": forms.TextInput(attrs=INPUT_ATTRS),
            "location": forms.TextInput(attrs=INPUT_ATTRS),
            "work": forms.TextInput(attrs=INPUT_ATTRS),
            "education": forms.TextInput(attrs=INPUT_ATTRS),
            "relationship": forms.TextInput(attrs=INPUT_ATTRS),
            "bio": forms.Textarea(attrs={**INPUT_ATTRS, "rows": 2}),
        }
