import profile
from django.urls import path
from .views import mainscreen, profile_list, profile

app_name = "posts"

urlpatterns = [
    path("", mainscreen, name="mainscreen"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]