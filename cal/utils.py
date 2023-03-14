from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django.db.models import Q
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(Q(start_time__day=day)|Q(end_time__day=day))
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'
	
	def create_html_table(self,events,withyear):
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}'
		return cal
  

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, user_id,withyear=True,):
		events = Event.objects.filter(start_time__year=self.year,username_id=user_id).filter(Q(start_time__month=self.month)|Q(end_time__month=self.month))
		cal_table=self.create_html_table(events,withyear)
		cal=f'<div>{cal_table}</div>'
		return cal