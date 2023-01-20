from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.urls import reverse_lazy
from .models import Notes
from .forms import NotesForm
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def notes_home(request):        
    return render(request, 'notes/notes_home.html', {})


@login_required(login_url=reverse_lazy('login'))
def add_notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            tests = form.save(commit=False)
            try:
                tests.username = request.user
            except Exception:
                pass
            tests.save()
            return HttpResponseRedirect('/academic/submitted_results/')
    else:    
      form = NotesForm()
    return render(request, 'notes/add_notes.html', {'form': form})

  