from django.shortcuts import render

# Create your views here.

from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse,reverse_lazy
from django.utils.safestring import mark_safe
import calendar
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .utils import Calendar
from .forms import EventForm


@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id=self.request.user.id
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True,user_id=user_id)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


@login_required(login_url=reverse_lazy('login'))
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id,username_id=request.user.id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        event_obj = form.save(commit=False)
        try:
            event_obj.username = request.user
        except Exception:
            pass
        event_obj.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def delete_event(request,event_id):
    user_id=request.user.id
    Event.objects.filter(username_id=user_id,id=event_id).delete()
    return HttpResponseRedirect('/calendar/')