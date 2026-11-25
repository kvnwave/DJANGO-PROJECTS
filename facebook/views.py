from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ProfileForm
from .models import Profile

SAMPLE_FRIENDS = (
    "Marco Reyes",
    "Althea Cruz",
    "Rafael Santos",
    "Bianca Lim",
    "Joshua Tan",
    "Camille Garcia",
    "Adrian Bautista",
    "Sofia Ramos",
    "Miguel Torres",
)

SAMPLE_STORIES = (
    ("mindcast", 0),
    ("vibeteller", 1),
    ("moodrealms", 2),
    ("inkdrop", 3),
    ("softpulse", 4),
    ("dreamwave", 5),
)

SAMPLE_POSTS = (
    {
        "time": "12h ago",
        "location": "Manila, Philippines",
        "caption": "soft hues, slow days, and a heart full of stillness \u2026",
        "likes": "107k",
        "liked_by": "@vibeteller, @moodrealms and others liked this post!",
        "media": True,
        "tone": 0,
    },
    {
        "time": "2d ago",
        "location": "Quezon City",
        "caption": "Manila, you were unreal. Salamat for the sold-out night.",
        "likes": "18.2k",
        "liked_by": "@inkdrop, @dreamwave and others liked this post!",
        "media": True,
        "tone": 2,
    },
    {
        "time": "5d ago",
        "location": "Tagaytay",
        "caption": "new music soon.",
        "likes": "5.4k",
        "liked_by": "@mindcast and others liked this post!",
        "media": False,
        "tone": 4,
    },
)


def profile_detail(request):
    profile = Profile.objects.first()
    if profile is None:
        raise Http404("No profile exists yet. Create one in the admin.")

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("facebook:profile")
        show_edit = True
    else:
        form = ProfileForm(instance=profile)
        show_edit = request.GET.get("edit") == "1"

    friends = [
        {
            "name": name,
            "initials": "".join(part[:1] for part in name.split()).upper(),
        }
        for name in SAMPLE_FRIENDS
    ]

    stories = [
        {
            "handle": handle,
            "initials": "".join(part[:1] for part in handle.split()).upper(),
            "tone": tone,
        }
        for handle, tone in SAMPLE_STORIES
    ]

    return render(
        request,
        "facebook/profile.html",
        {
            "profile": profile,
            "form": form,
            "show_edit": show_edit,
            "friends": friends,
            "stories": stories,
            "posts": SAMPLE_POSTS,
        },
    )
