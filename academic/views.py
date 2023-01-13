from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
import json
from .models import Tests
from .forms import TestsForm
from pages.models import Page


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def academic_home(request):        
    return render(request, 'academic/academic.html', {})


@login_required(login_url=reverse_lazy('login'))
def add_results(request):
    if request.method == 'POST':
        form = TestsForm(request.POST, request.FILES)
        if form.is_valid():
            tests = form.save(commit=False)
            try:
                tests.username = request.user
            except Exception:
                pass
            tests.save()
            return HttpResponseRedirect('/academic/submitted_results/')
    else:    
      form = TestsForm()
      return render(request, 'academic/add_results.html', {'form': form, 'page_list': Page.objects.all()})


@login_required(login_url=reverse_lazy('login'))
def submitted_results(request):
    user_id=request.user.id
    test_list=Tests.objects.filter(username=user_id).order_by('-id')
    return render(request, 'academic/submitted_results.html', {'test_list': test_list, 'page_list': Page.objects.all()})

@login_required(login_url=reverse_lazy('login'))
def view_results(request):
    user_id=request.user.id
    test_list=Tests.objects.filter(username=user_id).order_by('-id')
    return render(request, 'academic/view_results.html', {'users':['sam','raj']})



@login_required(login_url=reverse_lazy('login'))
def get_results_between_date_range(request):
    user_id=request.user.id
    test_list_query_set=Tests.objects.filter(username=user_id).values_list('test_subject','test_title')
    serialize_data=serialize("json", test_list_query_set)
    test_list_json=json.loads(serialize_data)
    return JsonResponse(test_list_json, status=200,safe=False)  
  