from django.forms import ModelForm,CharField,Textarea
from .models import Notes
from better_profanity import profanity
from django import forms



class NotesForm(ModelForm):
    required_css_class = 'required'
    title = CharField(max_length=100, label='Title')
    body_text = CharField(widget=Textarea,label='Notes')
    class Meta:
        model = Notes
        fields = ['title','body_text' ]
    
    def clean(self):
        cleaned_data = super().clean()
        body_text = cleaned_data.get('body_text')
        title = cleaned_data.get('title')
        if title is None or body_text is None:
            return cleaned_data
        if profanity.contains_profanity(body_text) or profanity.contains_profanity(title) :
            raise forms.ValidationError('Subject contains profanity ')
        return cleaned_data
