from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'