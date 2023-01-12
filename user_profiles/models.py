from django.db import models
#import _sha1
# Create your models here.

from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

SUBJECT_CHOICES = (
    ('Eco', 'Economics'),
    ('Art', 'Art'),
    ('Eng', 'English'),
    ('Mat', 'Maths'),
    ('Bio', 'Biology'),
    ('Phy', 'Physics'),
    ('Che', 'Chemistry'),
    ('Com', 'Computer Science'),
    ('Pol', 'Politics'),
    ('His', 'History'),
    ('Geo', 'Geography'),
    ('Psy', 'Psychology'),
    ('Fur', 'Further Maths'),
    ('Spa', 'Spanish'),
    ('PE', 'Physical Education'),
)

TARGET_CHOICES = (
    ('A*', 'A*'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

YEAR_CHOICES = (
    ('12', 'Year 12'),
    ('13', 'Year 13'),
)


    
#Can just hash firstname and lastname and user if password is hard to find and do
class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    year_group = models.CharField(max_length=10, choices=YEAR_CHOICES)
    # dob = [date, month, year] needs to be fixed!!!
    subject1 = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    subject2 = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    subject3 = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    subject4 = models.CharField(max_length=20, choices=SUBJECT_CHOICES, blank=True)
    target1 = models.CharField(max_length=4, choices=TARGET_CHOICES) 
    target2 = models.CharField(max_length=4, choices=TARGET_CHOICES) 
    target3 = models.CharField(max_length=4, choices=TARGET_CHOICES) 
    target4 = models.CharField(max_length=4, choices=TARGET_CHOICES, blank=True) 


    def __str__(self):
        return self.user.username

    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile2(user=instance)
        user_profile.save()

