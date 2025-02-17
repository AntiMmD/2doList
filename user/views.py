from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from .form import *
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
            return redirect(reverse('home'))
        else:
            return render(request, 'signUp.html', {'form': form, 'errors': form.errors} )

@csrf_exempt
def login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request, 'login.html',{'form' : form} )
    
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
                    return redirect(reverse('home'))
                    
            else: 
                    return render (request, 'login.html', { 'form':form,'error':'password is incorrect'}) 
                                
        else:
            return render (request, 'login.html', {'form':LoginForm(request.POST) , 'error':'invalid credintial'})          

        
@csrf_exempt
def logout(request):
        dj_logout(request)
        return redirect(reverse('login'))

