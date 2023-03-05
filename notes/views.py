from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.urls import reverse_lazy
import json
from .models import Notes
from .forms import NotesForm
from .utils import find_matching_notes 
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

@login_required(login_url=reverse_lazy('login'))
def search_notes(request):
    user_id=request.user.id
    search_text=request.GET['searchText']
    notes_list=[]
    all_notes=Notes.objects.filter(username=user_id).order_by('-id')
    for note in all_notes:
        temp_dict={'title':note.title,'body_text':note.body_text,'id':note.id}
        notes_list.append(temp_dict)
    matched_notes=find_matching_notes(search_text,notes_list)
    notes_json=json.dumps(matched_notes)
    return JsonResponse(json.loads(notes_json), status=200,safe=False)

@login_required(login_url=reverse_lazy('login'))
def update_note(request,note_id):
    user_id=request.user.id
    instance = get_object_or_404(Notes, username=user_id,id=note_id)
    form = NotesForm(request.POST or None,instance=instance)
    if request.method == 'POST':        
        if form.is_valid():
            notes = form.save(commit=False)
            try:
                notes.username = request.user
            except Exception:
                pass
            notes.save()
            return HttpResponseRedirect('/notes/view_notes/')
    return render(request, 'notes/add_notes.html', {'form': form})
    
@login_required(login_url=reverse_lazy('login'))
def delete_note(request,note_id):
    user_id=request.user.id
    Notes.objects.filter(username=user_id,id=note_id).delete()
    return HttpResponseRedirect('/notes/view_notes/')
