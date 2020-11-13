from django.urls import path
from . import views

urlpatterns = [
    path('', views.faxmachine_list, name='faxmachine_list'),
]