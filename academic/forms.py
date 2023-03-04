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
          'test_subject', 'test_title','test_given_date', 'test_marks', 'test_outof'
        ]
    def clean(self):
        cleaned_data = super().clean()
        test_marks = cleaned_data.get('test_marks')
        test_outOf = cleaned_data.get('test_outof')

        if test_marks and test_outOf and test_marks > test_outOf:
            raise forms.ValidationError('Marks should not be greater than out of')

        return cleaned_data