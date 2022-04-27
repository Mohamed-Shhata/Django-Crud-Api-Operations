from django import forms
from .models import Track, Student

# Auth forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'student_track')
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name', 'required': 'true', 'autofocus': 'true', 'maxlength': '50', 'pattern': '^[a-zA-Z]*$'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name', 'required': 'true', 'maxlength': '50', 'pattern': '^[a-zA-Z]*$'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age', 'required': 'false', 'maxlength': '2', 'pattern': '^[0-9]*$'}),
            'student_track': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Track', 'required': 'false'}),
        }

        
    class TrackForm(forms.ModelForm):
        class Meta:
            model = Track
            fields = ('name',)
            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Track Name', 'required': 'true'}),
            }
           

class UserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'required': 'true'}
    ))
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': 'true'}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username', 'required': 'true', 'maxlength': '50', 'pattern': '^[a-zA-Z0-9]*$'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'required': 'true', 'maxlength': '50', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name', 'required': 'true', 'maxlength': '50', 'pattern': '^[a-zA-Z]*$'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name', 'required': 'true', 'maxlength': '50', 'pattern': '^[a-zA-Z]*$'}),
        }