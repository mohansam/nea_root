from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from user_profiles.models import Profile2

@login_required(login_url=reverse_lazy('login'))
def revision_resources(request):      
    subjects=[]
    isSubjectUpdated=False
    enrolled_subjects=Profile2.objects.filter(user_id= request.user.id)[0]
    if enrolled_subjects.subject1:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject1.subject_name,'subject_id':enrolled_subjects.subject1.id})
    if enrolled_subjects.subject2:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject2.subject_name,'subject_id':enrolled_subjects.subject2.id})
    if enrolled_subjects.subject3:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject3.subject_name,'subject_id':enrolled_subjects.subject3.id})
    if enrolled_subjects.subject4:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject4.subject_name,'subject_id':enrolled_subjects.subject4.id})
    return render(request, 'revision/list_subjects.html', {'subjects':subjects,'isSubjectUpdated':isSubjectUpdated})


 
@login_required(login_url=reverse_lazy('login'))
def list_topics(request,subject_id):      
    topics=['Oops','Btree']  
    return render(request, 'revision/list_topics.html', {'topics':topics})


@login_required(login_url=reverse_lazy('login'))
def list_resources(request):      
    resources=['https://stackoverflow.com/questions/18413660/html-how-to-insert-links-into-ordered-unordered-lists','science']  
    return render(request, 'revision/list_resources.html', {'resources':resources})