from django import forms
from .models import Text_Post
from better_profanity import profanity


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

    def clean_body(self):
        body = self.cleaned_data['body']
        if profanity.contains_profanity(body):
            raise forms.ValidationError('Subject contains profanity')
        return body