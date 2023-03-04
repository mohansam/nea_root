from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
import json
from .models import Tests
from .forms import TestsForm
import datetime


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
        return render(request, 'academic/add_results.html', {'form': form})        
    else:    
      form = TestsForm()
      return render(request, 'academic/add_results.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
def submitted_results(request):
    user_id=request.user.id
    test_list=Tests.objects.filter(username=user_id).order_by('-id')
    return render(request, 'academic/submitted_results.html', {'test_list': test_list})

@login_required(login_url=reverse_lazy('login'))
def view_results(request):
    return render(request, 'academic/view_results.html')


@login_required(login_url=reverse_lazy('login'))
def update_test(request,test_id):
    user_id=request.user.id
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
        return render(request, 'academic/add_results.html', {'form': form})        
    else:
      instance = get_object_or_404(Tests, username=user_id,id=test_id)
      form = TestsForm(None,instance=instance)
      return render(request, 'academic/add_results.html', {'form': form})
    
@login_required(login_url=reverse_lazy('login'))
def delete_test(request,test_id):
    user_id=request.user.id
    Tests.objects.filter(username=user_id,id=test_id).delete()
    return HttpResponseRedirect('/academic/submitted_results/')

@login_required(login_url=reverse_lazy('login'))
def get_results_between_date_range(request):
    user_id=request.user.id
    start_duration=request.GET['startDuration']
    end_duration=request.GET['endDuration']
    try:
        datetime.datetime.strptime(start_duration, '%Y-%m-%d')
        datetime.datetime.strptime(end_duration, '%Y-%m-%d')
        test_list_query_set=Tests.objects.filter(username=user_id,test_given_date__gte=start_duration,test_given_date__lt=end_duration)
    except ValueError:
        test_list_query_set=Tests.objects.filter(username=user_id)
    result_tracker_dict={}
    subject_percentage_dict={}
    for test_list in test_list_query_set:
           subject_name=test_list.test_subject.subject_name
           if  subject_name not in result_tracker_dict:
              result_tracker_dict[subject_name]={'test_marks':0,'test_outof':0}
           result_tracker_dict[subject_name]['test_marks']+=int(test_list.test_marks)
           result_tracker_dict[subject_name]['test_outof']+=int(test_list.test_outof)
    for subject_key in result_tracker_dict:
        subject_percentage_dict[subject_key]=(result_tracker_dict[subject_key]['test_marks']/result_tracker_dict[subject_key]['test_outof'])*100
    test_list_json=json.dumps(subject_percentage_dict)
    return JsonResponse(json.loads(test_list_json), status=200,safe=False)  
  