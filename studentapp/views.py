from django.shortcuts import render,redirect
from django.views import View
from studentapp.forms import *
from django.contrib.auth.forms import UserCreationForm
# from studentapp.forms import SignupForm,signinForm
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate



class SignUpView(CreateView):
    template_name="studentSignup.html"
    form_class=SignupForm
    success_url=reverse_lazy('signin')

class SigninView(FormView):
    template_name='studentSignin.html'
    form_class=signinForm
    def post(self,request):
        form_data=signinForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
        if user:
            return redirect('shome')
        else:
            return redirect('signin')
        
class StudentHomeView(ListView):
    template_name='student_home.html'
    model=StudentModel
    context_object_name='slist'

class AddStudentView(CreateView):
    template_name='addStudent.html'
    form_class=StudentForm
    def post(self,request):
        form_data=StudentForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('shome')
        return render(request,"addStudent.html",{"form":form_data})
    




     



   

    





    



    
    

