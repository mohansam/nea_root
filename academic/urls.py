from django.urls import path

from . import views

urlpatterns = [
    path('', views.academic_home, name='academic-request'),
    path('add_results/', views.tests_req, name='add-request'),
]