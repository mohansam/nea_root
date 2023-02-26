from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes_home, name='notes-home'),
    path('add_notes/', views.add_notes, name='add-notes'),
    path('view_notes/', views.view_notes, name='add-notes'),
    path('search_notes/', views.search_notes, name='search-notes'),
]