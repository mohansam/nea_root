import threading
import time
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.utils import timezone
from .models import Event

class EventReminderScheduler:
    def __init__(self, interval_hours):
        self.interval_hours = interval_hours
        self._timer = None
        self._is_running = False

    def start(self):
        if not self._is_running:
            self._is_running = True
            self._schedule_next_event()

    def stop(self):
        if self._is_running:
            self._timer.cancel()
            self._is_running = False

    def _schedule_next_event(self):
        today = timezone.now().date()
        events = Event.objects.filter(start_time__date=today)
        for event in events:
            message = f"You have an event today: {event.title} ({event.start_time} - {event.end_time})"
            user_email=event.username.email
            # just mocking email call, didn't setup SMTP server
            send_mail(
                'Upcoming Event',
                message,
                'mohanraj.mk1111@gmail.com',
                [user_email],
                fail_silently=True,
            )
            print('email send to user')

        self._timer = threading.Timer(self.interval_hours * 3600, self._schedule_next_event)
        self._timer.start()
