from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Track, Student
from .forms import StudentForm,UserForm


#rest_framework api imports here

from .serializers import StudentSerializer, TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# auth imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Ouath views here

def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            userName = request.POST.get('username')
            userPassword = request.POST.get('password')
            user = authenticate(username=userName, password=userPassword)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'djapp/login.html')


def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method == 'POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + \
                    signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'djapp/signup.html', context)


def signOut(request):
    logout(request)
    return redirect('login')

@api_view(['GET'])
def api_all_student(request):
    all_students = Student.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_one_student(request, std_id):
    student = Student.objects.get(id=std_id)
    serializer = StudentSerializer(student,many=False)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def api_add_student(request):
    std_ser = StudentSerializer(data=request.data)
    if std_ser.is_valid():
        std_ser.save()
        return redirect('api-all')
    else :
        return Response(std_ser.errors)

@api_view(['PUT', 'GET'])
def api_edit_student(request, std_id):
    print("hello")
    std = Student.objects.get(id=std_id)
    print(std)
    
    std_ser = StudentSerializer(instance=std, data=request.data)
    print(std_ser)
    if std_ser.is_valid():
        std_ser.save()
        return redirect('api-all')
    else :
        return Response(std_ser.errors)
@api_view(['DELETE','GET'])       
def api_delete_student(request, std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    return Response("Student Deleted")

# Create your views here.

def home(request):
    all_students= Student.objects.all()
    context={'all_students':all_students}
    return render(request,'djapp/home.html',context)  
    # return HttpResponse('<h1>Hello from home function </h1>') 

def show(request,student_id):
    st= Student.objects.get(id=student_id)
    context={'student':st}
    return render(request,'djapp/show.html',context)

def delete(request,student_id):
    st= Student.objects.get(id=student_id)
    st.delete()
    return redirect('home')

def add_student(request):
    st_form=StudentForm()
    if request.method=='POST':
        st_form=StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context={'st_form':st_form}
    return render(request,'djapp/add.html',context)

def editStudent (request,student_id):
    st= Student.objects.get(id=student_id)
    st_form=StudentForm(instance=st)
    if request.method=='POST':
        st_form=StudentForm(request.POST,instance=st)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context={'st_form':st_form}
    return render(request,'djapp/add.html',context)