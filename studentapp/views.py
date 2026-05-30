from django.shortcuts import render
from django.views import View
from studentapp.forms import *

# Create your views here.
class studentHomeView(View):
    def get(self,request):
        return render(request,"student_home.html")
    
class studentSignUpView(View):
    def get(self,request):
        form = StudentForm
        return render(request,"studentSignup.html",{"form":form})
    
class studentSignInView(View):
    def get(self,request):
        form = signinForm
        return render(request,"studentSignIn.html",{"form":form})



    #  form = UserForm()
    #     return render(request,"signup.html",{"form":form})
    # def post(self,request):
    #     form_data = UserForm(data=request.POST)
    #     print(form_data)
    #     if form_data.is_valid():
    #         form_data.save()
    #         messages.success(request,"SignUp Sucessfull ")
    #         return redirect('home')
    #     # messages.warning(request,"Error,Please Signup again !")
    #     return render(request,"signup.html",{"form":form_data})
    
    

