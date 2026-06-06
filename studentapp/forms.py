# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from studentapp.models import * 

# class SignupForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=["first_name","last_name","username","email","password1","password2"]

# class signinForm(forms.Form):
#     username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
#     password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model=StudentModel
#         fields='__all__'
    
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from studentapp.models import *

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User  
#         fields = ["first_name","last_name","username", "email", "password1", "password2"]


# class signinForm(forms.Form):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"}))


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = StudentModel
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         for field in self.fields.values():
#             field.widget.attrs.update({
#                 'class': 'w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
#             })


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentModel  # Ningalude model import cheyyuka

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    # Ella fields-num tailwind classes apply cheyyan __init__ add cheyyuka
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            })

class signinForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
    }))

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            })