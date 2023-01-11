from django.urls import path

from . import views

urlpatterns = [
    path('', views.revision_resources, name='revision-request'),
    path('topics/1', views.list_topics, name='topics-request'),
    path('topics/resources/1', views.list_resources, name='resources-request'),
]