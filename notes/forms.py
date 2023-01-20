from django.forms import ModelForm,CharField,Textarea
from .models import Notes

class NotesForm(ModelForm):
    required_css_class = 'required'
    title = CharField(max_length=100, label='Title')
    body_text = CharField(widget=Textarea,label='Notes')
    class Meta:
        model = Notes
        fields = ['title','body_text' ]