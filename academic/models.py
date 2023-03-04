from django.db import models

# Create your models here.

from django.contrib.auth.models import User



SUBJECT_CHOICES = (
    ('Economics', 'Economics'),
    ('Art', 'Art'),
    ('English', 'English'),
    ('Maths', 'Maths'),
    ('Biology', 'Biology'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Computer Science', 'Computer Science'),
    ('Politics', 'Politics'),
    ('History', 'History'),
    ('Geography', 'Geography'),
    ('Psychology', 'Psychology'),
    ('Further Maths', 'Further Maths'),
    ('Spanish', 'Spanish'),
    ('Physical Education', 'Physical Education'),
)

class Subjects(models.Model):
    subject_name=models.CharField(max_length=20, choices=SUBJECT_CHOICES,unique=True)
    
    def __str__(self):
        return str(self.subject_name)

class Topics(models.Model):
    subject=models.ForeignKey(Subjects, blank=True, null=True, on_delete=models.CASCADE)
    topics_name=models.CharField(max_length=100)
    resource_url=models.URLField()
    resource_name=models.CharField(max_length=100)



class Tests(models.Model):
    test_subject =models.ForeignKey(Subjects, blank=True, null=True, on_delete=models.CASCADE)
    test_title = models.CharField(max_length=100)
    test_given_date= models.DateTimeField()
    test_marks = models.DecimalField(decimal_places=0, max_digits=4)
    test_outof =  models.DecimalField(decimal_places=0, max_digits=4)
    #test_percentage = round(test_marks/test_outof)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)