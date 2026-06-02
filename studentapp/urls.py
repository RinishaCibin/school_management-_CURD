from django.urls import path
from studentapp.views import *

urlpatterns = [
     path('',SignUpView.as_view(),name='signup'),
     path('shome',StudentHomeView.as_view(),name='shome'),
     path('addstudent',AddStudentView.as_view(),name='addstudent')
   
  
  
]