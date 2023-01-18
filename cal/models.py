from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse

EVENT_PRIORITY=( ('HIGH', 'HIGH'),
    ('Medium', 'Medium'),
    ('Low', 'Low'))

class Event(models.Model):
    title = models.CharField(max_length=100)
    priority=models.CharField(max_length=20, choices=EVENT_PRIORITY)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        event_type_class={'HIGH':'eventP1','Medium':'eventP2','Low':'eventP3'}
        return f'<a  class="{event_type_class[self.priority]}" href="{url}"> <b>{self.title}</b> </a>'