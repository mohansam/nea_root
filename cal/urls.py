from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
	path('event/update_event/<int:event_id>', views.event, name='update_event'),
    path('event/delete_event/<int:event_id>', views.delete_event, name='delete_event'),


]