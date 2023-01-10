from django import forms
from django.forms import ModelForm
from .models import Profile2
from django.contrib.auth.models import User


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']



class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile2
        fields = ['avatar', 'firstname', 'lastname', 'year_group',
        'subject1', 'subject2', 'subject3', 'subject4',
        'target1', 'target2', 'target3', 'target4'] 

