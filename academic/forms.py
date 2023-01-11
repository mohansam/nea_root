from django import forms
from django.forms import ModelForm,DateInput
from .models import Tests

class TestsForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Tests
        widgets = {
      'test_given_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d')}
        fields = [
          'test_subject', 'test_title','test_given_date', 'date', 'month', 'year', 'test_marks', 'test_outof'
        ]