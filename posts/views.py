from cProfile import Profile
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Text_Post, Posts_Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def mainscreen(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts:mainscreen")

    followed_posts = Text_Post.objects.filter(
        user__posts_profile__in=request.user.posts_profile.follows.all()
    ).order_by("-created_at")

    return render(request, "posts/mainscreen.html", {"form": form, "posts": followed_posts},
    )

def profile_list(request):
    profiles = Posts_Profile.objects.exclude(user=request.user)
    return render(request, "posts/profile_list.html", {"profiles":profiles})

#profile is the variable that you’re passing in your context dictionary to render() in profile(). It holds the information that you pulled from your database about a user profile.
def profile(request, pk):
    profile = Posts_Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.posts_profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "posts/profile.html", {"profile": profile})

