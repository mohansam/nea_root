from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Posts_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username 

#Decorator is used; a function that takes another function and extends the behaviour of the latter function without explicity modifying it.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Posts_Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.posts_profile)
        #Less efficient version of line 28: user_profile.follows.set([instance.posts_profile.id])
        user_profile.save()


class Text_Post(models.Model):
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    #next = models.OneToOneField("self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="previous")

    
    #can change f strings into something more personalised or change everything to f strings
    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )

#previous_post = Text_Post.objects.filter(user=User).order_by("-created_at").first()
#new_post = Text_Post.objects.create(user=User, body=new_post.body)
#if previous_post:
    #previous_post.next = new_post
    #previous_post.save()