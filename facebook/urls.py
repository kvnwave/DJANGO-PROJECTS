from django.urls import path

from . import views

app_name = "facebook"

urlpatterns = [path("", views.profile_detail, name="profile")]
