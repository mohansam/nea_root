from django.db import models

# Create your models here.

from django.contrib.auth.models import User


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


class Revision(models.Model):
    subject_resource = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    chapter_no = models.DecimalField(decimal_places=0, max_digits=3, default=0)
    chapter_title = models.CharField(max_length=100)
    notes = models.URLField(blank=True)
    flashcards = models.URLField(blank=True)
    videos = models.URLField(blank=True)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)