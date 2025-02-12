from django.shortcuts import render,redirect
from .form import *
from task.models import Task
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def signUp(request):
    form = SignUpForm()
    if request.method == 'GET':
        return render(request, 'signUp.html', {'form': form } )

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            form.save()
            user = User.objects.get(username=username)
            dj_login(request, user)
            return redirect('/user/home')
        else:
            return render(request, 'signUp.html', {'form': form, 'errors': form.errors} )

@csrf_exempt
def login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request, 'login.html',{'form' : LoginForm()} )
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return render (request, 'login.html', {'form':LoginForm() ,'error':'user does not exist'})   

            if user.check_password(password):
                    dj_login(request, user)
                    return redirect('/user/home')
                    
            else: 
                    return render (request, 'login.html', { 'form':form,'error':'password is incorrect'}) 
                                
        else:
            return render (request, 'login.html', {'form':LoginForm(request.POST) , 'error':'invalid credintial'})          

        
@csrf_exempt
def logout(request):
    dj_logout(request)
    return redirect('/user/login')

@csrf_exempt
@login_required(login_url='/user/login')
def home(request):
    if request.method=='GET':
        tasks = request.user.tasks.all()
        return render(request ,'home.html', {'tasks': tasks}) 


@csrf_exempt
@login_required(login_url='/user/login')
def addTask(request):

    if request.method == 'GET':
        form = CreateTask()
        return render(request, 'createTask.html', {'form': form})
    
    elif request.method == 'POST':
        form = CreateTask(request.POST)

        if form.is_valid():
            request.user.tasks.create(**form.cleaned_data , user = request.user)
            return redirect('/user/home')
        else:
            return redirect('/user/home')
    else:
        HttpResponse("only get and post method is allowed")


@csrf_exempt
@login_required(login_url='/user/login')
def deleteTask(request, id):

    if request.method == 'POST':    
        request.user.tasks.get(id=id).delete()
        return redirect('/user/home')
    
    return redirect('/user/home')


@csrf_exempt
@login_required(login_url='/user/login')
def updateTask(request,id):

    task = request.user.tasks.get(id=id)
    if request.method == 'GET':
        form = CreateTask(instance = request.user.tasks.get(id=id))
        return render(request, 'updateTask.html', {'form': form})
    
    if request.method == 'POST':
        form = CreateTask(request.POST, instance = task )

        if form.is_valid():
            task= form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/user/home')
        else:
            return redirect('/user/home')
    else:
        HttpResponse("only get and post method is allowed")

    
def searchTask(request):
    error = ''
    task_name = request.GET.get('task_name', '')  
    
    if task_name:

        tasks = request.user.tasks.filter(name = task_name)
        if tasks.count()==0:
            tasks = request.user.tasks.all()
            error = 'no item mathced'  
        
    else:
        tasks = request.user.tasks.all()  

    return render(request, 'home.html', {'tasks': tasks, 'error':error})