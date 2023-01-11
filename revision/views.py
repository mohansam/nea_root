from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def revision_resources(request):      
    subjects=['Math','science']  
    return render(request, 'revision/list_subjects.html', {'subjects':subjects})


 
@login_required(login_url=reverse_lazy('login'))
def list_topics(request):      
    topics=['Oops','Btree']  
    return render(request, 'revision/list_topics.html', {'topics':topics})


@login_required(login_url=reverse_lazy('login'))
def list_resources(request):      
    resources=['https://stackoverflow.com/questions/18413660/html-how-to-insert-links-into-ordered-unordered-lists','science']  
    return render(request, 'revision/list_resources.html', {'resources':resources})