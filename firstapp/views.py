from multiprocessing import context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import Student, Track
from .forms import StudentForm ,UserForm

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#############################api######################
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def api_all_student(request):
     all_st = Student.objects.all()
     st_ser=StudentSerializer(all_st,many=True)
     return Response(st_ser.data)

@api_view(['GET'])    
def api_one_student(request,st_id):
    st=Student.objects.get(id=st_id)
    st_ser=StudentSerializer(st,many=False)
    return Response(st_ser.data)

@csrf_exempt
@api_view(['POST'])
def api_add_student(request):
     st_ser=StudentSerializer(data=request.data)
     if st_ser.is_valid():
            st_ser.save()
            return redirect('api-all')
@csrf_exempt
@api_view(['POST'])
def api_edit_student(request,st_id):
    st=Student.objects.get(id=st_id)
    st_ser=StudentSerializer(data=request.data,instance=st)
    if st_ser.is_valid():
            st_ser.save()
            return redirect('api-all')
@csrf_exempt
@api_view(['DELETE'])
def api_del_student(request,st_id):
     st=Student.objects.get(id=st_id)
     st.delete()
     return Response('student delete successfly')

    

def home(request):
    all_students = Student.objects.all()
    context = {'student_list':all_students}
    return render(request, 'firstapp/home.html',context)

def show(request , st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st }
    return render(request,'firstapp/show.html',context)


def deletest(request , st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return redirect('home')

def addStudent(request):
    st_form = StudentForm()
    if request.method=='POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'st_form':st_form}
    return render(request, 'firstapp/add.html',context)

def edit(request, st_id):
   st = Student.objects.get(id=st_id)
   st_form = StudentForm(instance=st)
   if request.method=='POST':
        st_form = StudentForm(request.POST,instance=st)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
   context = {'st_form':st_form}
   return render(request, 'firstapp/add.html',context)

def signuppg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form=UserForm()
        if(request.method=='POST'):
            signup_form=UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg='user account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context={'signup_form' : signup_form}
        return render(request ,'firstapp/signup.html', context)

def loginpg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if(request.method=='POST'):
            name=request.POST.get('username')
            passwd=request.POST.get('password')
            user=authenticate(username=name ,password=passwd)
            if user is not None:
                login(request,user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                messages.info(request ,"user name or password is incorrect")
        return render(request ,'firstapp/login.html')
    
def signoutpg(request):
    logout(request)
    return redirect('login')




