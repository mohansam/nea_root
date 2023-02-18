from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def homepage(request):
    return render(request, 'home.html')