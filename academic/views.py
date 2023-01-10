from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect

from .models import Tests
from .forms import TestsForm
from pages.models import Page


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def academic_home(request):
    submitted = False
    if request.method == 'POST':
        form = TestsForm(request.POST, request.FILES)
        if form.is_valid():
            tests = form.save(commit=False)
            try:
                tests.username = request.user
            except Exception:
                pass
            tests.save()
            return HttpResponseRedirect('/academic/?submitted=True')
    else:
        form = TestsForm()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'academic/academic.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def tests_req(request):
    submitted = False
    if request.method == 'POST':
        form = TestsForm(request.POST, request.FILES)
        if form.is_valid():
            tests = form.save(commit=False)
            try:
                tests.username = request.user
            except Exception:
                pass
            tests.save()
            return HttpResponseRedirect('/academic/?submitted=True')
    else:
        form = TestsForm()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'academic/add_results.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})