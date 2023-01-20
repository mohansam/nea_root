from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=60)
    update_date = models.DateTimeField('Last Updated')
    body_text = models.TextField('Page Content', blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title