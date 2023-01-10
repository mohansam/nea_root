from django import forms
from django.forms import ModelForm
from .models import Tests

class TestsForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Tests
        fields = [
            'test_subject', 'test_title', 'date', 'month', 'year', 'test_marks', 'test_outof'
        ]