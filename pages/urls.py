from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('need_help', views.need_help, name='need_help'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('<str:pagename>', views.index, name='home'),
    
]