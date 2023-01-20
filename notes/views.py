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
            notes = form.save(commit=False)
            try:
                notes.username = request.user
            except Exception:
                pass
            notes.save()
            return HttpResponseRedirect('/notes/view_notes/')
    else:    
      form = NotesForm()
    return render(request, 'notes/add_notes.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def view_notes(request):
    user_id=request.user.id
    all_notes=Notes.objects.filter(username=user_id).order_by('-id')
    return render(request, 'notes/view_notes.html', {'all_notes': all_notes})
  