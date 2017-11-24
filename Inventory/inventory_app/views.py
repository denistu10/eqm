from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def get_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('ok')
                return redirect('/management')
            else:
                status = "Аккаунт заблокирован"
                return render(request,'Error.html', locals())
        else:
            status = "Не верный логин или пароль"
            return render(request, 'Error.html', locals())



def logout_views(request):
    logout(request)
    return redirect('/')

@login_required()
def management_views(request):
    equipment = Equipment.objects.all()
    users = Employees.objects.all()
    print(Equipment.objects.all().values())
    return render(request,'panel.html', locals())


