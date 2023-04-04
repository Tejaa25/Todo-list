from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
from django.contrib.auth.models import User
from .models import todo
def firstpage(request):
    return render(request,"todoApp/firstpage.html")
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been created successfully")
        return redirect("/signin")
        
    return render(request,"todoApp/signup.html")
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            obj=todo.objects.filter(User=request.user)
            return redirect('/todo')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('firstpage')
    return render(request,"todoApp/signin.html")
def view(request):
    obj=todo.objects.filter(User=request.user)
    return render(request,'todoApp/todolist.html',{'obj':obj})

def add(request):
    obj=todo.objects.filter(User=request.user)
    new_todo=None
    if request.method=='POST':
        form=forms.todoForm(request.POST)
        if form.is_valid():
            new_todo=form.save(commit=False)
            new_todo.User=request.user
            uname=request.user
            new_todo.save()
            return redirect('/todo')
    else:
        form=forms.todoForm()
    return render(request,'todoApp/todo.html',{'form':form})

def delete(request,id):
    obj=todo.objects.get(id=id)
    obj.delete()
    return redirect('/todo')
def update(request,id):
    form=forms.todoForm()
    obj=todo.objects.get(id=id)
    if request.method=='POST':
        form=forms.todoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    else:
        return render(request,'todoApp/update.html',{'form':form,'obj':obj})
def logout(request):
    auth_logout(request)
    messages.success(request,'logged out successfully')
    return redirect('/')
        


    