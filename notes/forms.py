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

    def clean_body_text(self):
        body_text = self.cleaned_data['body_text']
        if profanity.contains_profanity(body_text):
            raise forms.ValidationError('Subject contains profanity')
        return body_text