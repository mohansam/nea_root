from django.forms import ModelForm, DateInput
from django import forms
from cal.models import Event
from datetime import datetime

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['title','description','start_time','end_time','priority']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

  def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_time')
        end_datetime = cleaned_data.get('end_time')

        if start_datetime and end_datetime:
            if isinstance(start_datetime, datetime) and isinstance(end_datetime, datetime):
                if end_datetime <= start_datetime:
                  raise forms.ValidationError('End time should be greater than start time')
            else:
                raise forms.ValidationError('Both start and end datetime should be datetime objects')

        return cleaned_data