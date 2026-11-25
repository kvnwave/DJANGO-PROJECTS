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

SAMPLE_POSTS = (
    {
        "time": "2h",
        "text": "\u201cToo Much Of A Good Thing\u201d is out now on all streaming platforms. Thank you for putting it at number one.",
        "likes": "2.4K",
        "comments": "128",
        "shares": "34",
        "media": True,
        "tone": 0,
    },
    {
        "time": "Yesterday at 9:14 PM",
        "text": "Manila, you were unreal. Salamat for the sold-out night.",
        "likes": "18K",
        "comments": "342",
        "shares": "96",
        "media": True,
        "tone": 2,
    },
    {
        "time": "Monday at 11:02 AM",
        "text": "New music soon.",
        "likes": "5.2K",
        "comments": "87",
        "shares": "21",
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

    return render(
        request,
        "facebook/profile.html",
        {
            "profile": profile,
            "form": form,
            "show_edit": show_edit,
            "friends": friends,
            "posts": SAMPLE_POSTS,
        },
    )
