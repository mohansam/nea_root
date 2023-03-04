from django.shortcuts import render
from datetime import datetime, timedelta, date
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from cal.models import Event

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def homepage(request):
    today_date=datetime.now()
    user_id=request.user.id
    current_month_events = Event.objects.filter(start_time__year=today_date.year, start_time__month=today_date.month , username_id=user_id)
    todays_event_day = current_month_events.filter(Q(start_time__day=today_date.day)|Q(end_time__day=today_date.day))
    return render(request, 'home.html',{'events':current_month_events})