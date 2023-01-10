from django import forms
from .models import Text_Post

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True,
    widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Type up something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Text_Post
        exclude = ("user", )