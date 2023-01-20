from email import message
from django import forms

class NotesForm(forms.Form):
    title = forms.CharField(max_length=100, label='Title')
    body_text = forms.CharField(widget=forms.Textarea,label='Notes')

