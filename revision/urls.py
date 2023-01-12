from django.urls import path

from . import views

urlpatterns = [
    path('', views.revision_resources, name='revision-request'),
    path('topics/<int:subject_id>', views.list_topics, name='topics-request'),
    path('topics/resources/<str:topics_name>', views.list_resources, name='resources-request'),
]