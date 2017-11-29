from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
import csv
from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html', locals())
    else:
        return redirect('/inventory')

def get_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('ok')
                return redirect('/inventory')
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
def inventory_views(request):
    equipment = Equipment.objects.filter(is_active=True)
    return render(request, 'inventory.html', locals())


@login_required()
def generate_csv(request):
    file = 'inventory.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    equipment = Equipment.objects.filter(is_active=True)
    writer = csv.writer(response, delimiter=';')
    for eq in equipment:
        writer.writerow([eq.inventory_number, eq.name,eq.type.type,eq.user.user, eq.is_license,eq.list_software])

    return response
