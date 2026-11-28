from datetime import date

from django.db import migrations


def seed_profile(apps, schema_editor):
    Profile = apps.get_model("facebook", "Profile")
    if Profile.objects.exists():
        return
    Profile.objects.create(
        first_name="Nikki",
        last_name="Santos",
        username="nikkisantos",
        bio="Musician — \u201cToo Much Of A Good Thing\u201d out now.",
        location="Manila, Philippines",
        work="Musician at Wave Records",
        education="University of Santo Tomas",
        relationship="Single",
        friends_count=498,
        joined_on=date(2018, 5, 12),
    )


def remove_seed(apps, schema_editor):
    Profile = apps.get_model("facebook", "Profile")
    Profile.objects.filter(username="nikkisantos").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("facebook", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_profile, remove_seed),
    ]
