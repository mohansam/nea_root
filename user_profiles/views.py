from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponseRedirect

from .models import Profile2

from django.views.generic.edit import CreateView
# The UserCreationForm automatically hashes the password, 
# and also uses two password fields that look if the passwords match, 
# and presents the passwords as a password field.
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile2)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully')
        #elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error(request, 'Unable to update profile')
        return redirect(to='user_profiles-profile')
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile2)
    
    return render(request, 'user_profiles/profile2.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class=PasswordChangeForm
    template_name = 'user_profiles/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('password_success')

def change_password_success(request):
    return render(request,'user_profiles/change_password_success.html',{})