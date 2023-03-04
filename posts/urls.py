import profile
from django.urls import path
from .views import mainscreen, profile_list, profile,update_post,delete_post

app_name = "posts"

urlpatterns = [
    path("", mainscreen, name="mainscreen"),
    path("profile_list/", profile_list, name="profile_list"),
    path('update_post/<int:post_id>', update_post, name='update_post'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path("profile/<int:pk>", profile, name="profile"),
]