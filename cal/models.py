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
        event_type_class={'HIGH':'eventP1','Medium':'eventP2','Low':'eventP3'}
        str= f'<p class="{event_type_class[self.priority]}"><b>{self.title}</b> </p>'
        edit= f'<a href="/event/update_event/{self.id}"><i class="material-icons" style="font-size:30px;color:rgb(0, 255, 115)">update</i> </a>'
        delete_str=f'<a href="/event/delete_event/{self.id}"> <i class="material-icons" style="font-size:30px;color:red">delete_forever</i></a>'
        return str+edit+delete_str
               
                