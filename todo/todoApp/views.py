from django.shortcuts import render,redirect
from . import forms
# Create your views here.
from .models import todo
def view(request):
    obj=todo.objects.all()
    form=forms.todoForm()
    return render(request,'todoApp/todolist.html',{'obj':obj,'form':form})
def add(request):
    if request.method=='POST':
        form=forms.todoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=forms.todoForm()
    return render(request,'todoApp/todo.html',{'form':form})

def delete(request,id):
    obj=todo.objects.get(id=id)
    obj.delete()
    return redirect('/')
def update(request,id):
    form=forms.todoForm()
    obj=todo.objects.get(id=id)
    if request.method=='POST':
        form=forms.todoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request,'todoApp/update.html',{'form':form,'obj':obj})
        


    