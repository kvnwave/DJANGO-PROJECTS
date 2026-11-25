from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import PostForm, ProfileForm
from .models import Profile

SAMPLE_FRIENDS = (
    "Ramy Mirza",
    "Victoire Desgraves",
    "Letty Price",
    "Anthony Ribben",
    "Griffin Harley",
    "Evie Brooke",
    "Professor Lovell",
    "Professor Playfair",
    "Mrs. Piper",
)

SAMPLE_STORIES = (
    ("ramy", 0),
    ("victoire", 1),
    ("letty", 2),
    ("griffin", 3),
    ("anthony", 4),
    ("evie", 5),
)


def profile_detail(request):
    profile = Profile.objects.first()
    if profile is None:
        raise Http404("No profile exists yet. Create one in the admin.")

    show_edit = request.GET.get("edit") == "1"
    form = ProfileForm(instance=profile)
    post_form = None

    if request.method == "POST":
        if request.POST.get("action") == "post":
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.profile = profile
                post.save()
                messages.success(request, "Your post has been shared.")
                return redirect("facebook:profile")
        else:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Your profile has been updated.")
                return redirect("facebook:profile")
            show_edit = True

    if post_form is None:
        post_form = PostForm()
    post_form.fields["content"].widget.attrs["placeholder"] = (
        f"What's on your mind, {profile.first_name}?"
    )

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
            "post_form": post_form,
            "posts": profile.posts.all(),
        },
    )
