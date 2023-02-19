from django.apps import AppConfig

class CalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cal'

    def ready(self):
        from .models import Event
        from .send_reminder import EventReminderScheduler
        # Initialize and start the event reminder scheduler
        scheduler = EventReminderScheduler(interval_hours=24)
        scheduler.start()

