from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from .models import Profile2


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile2.save()
    except:
        pass
        


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile2.save()
