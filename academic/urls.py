from django.urls import path

from . import views

urlpatterns = [
    path('', views.academic_home, name='academic-request'),
    path('add_results/', views.add_results, name='add-request'),
    path('view_results/', views.view_results, name='view-request'),
    path('submitted_results/', views.submitted_results, name='submitted-request'),
    path('update_test/<int:test_id>', views.update_test, name='update_test'),
    path('delete_test/<int:test_id>', views.delete_test, name='update_test'),
    path('get_results_between_date_range/', views.get_results_between_date_range, name='results-between-date-request')
]