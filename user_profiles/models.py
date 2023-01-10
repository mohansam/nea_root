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

DATE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

MONTH_CHOICES = (
    ('Jan', '1'),
    ('Feb', '2'),
    ('Mar', '3'),
    ('Apr', '4'),
    ('May', '5'),
    ('Jun', '6'),
    ('Jul', '7'),
    ('Aug', '8'),
    ('Sep', '9'),
    ('Oct', '10'),
    ('Nov', '11'),
    ('Dec', '12'),
)

BIRTH_YEAR_CHOICES = (
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
)
    
#Can just hash firstname and lastname and user if password is hard to find and do
class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    firstname = models.CharField(max_length=100)
    #firstname_salt = models.CharField(max_length=8, null=True)
    #firstname_hash = models.CharField(max_length=40, null=True)
    lastname = models.CharField(max_length=100)
    #lastname_salt = models.CharField(max_length=8, null=True)
    #lastname_hash = models.CharField(max_length=40, null=True)
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

    #def check_firstname(self, password):
         #return _sha1.sha(self.password_salt + password).hexdigest() == self.password_hash

    #def check_lastname(self, password):
         #return _sha1.sha(self.password_salt + password).hexdigest() == self.password_hash

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

