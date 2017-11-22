from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


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
                return HttpResponseRedirect('/')
            else:
                status = "Аккаунт заблокирован"
                return render(request,'Error.html', locals())
        else:
            status = "Не верный логин или пароль"
            return render(request, 'Error.html', locals())
