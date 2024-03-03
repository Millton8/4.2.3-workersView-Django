from django.shortcuts import render
from datetime import datetime
from .models import WorkerInfo,Rezofwork
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db import connection
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 



def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT workerinfo.uniq,workerinfo.name,project,workerinfo.workerstatus FROM rezofwork LEFT JOIN workerinfo ON rezofwork.uniq=workerinfo.uniq WHERE rezofwork.id=(SELECT MAX(id) FROM rezofwork WHERE rezofwork.uniq=workerinfo.uniq) ORDER BY workerstatus DESC;")
        row = cursor.fetchall()     
    return render(request, "index.html",{"people":row})

def rezofwork(request):
    data=Rezofwork.objects.all()
    for i in data:
        if i.salary is not None:
            i.salary=i.salary.replace("?","₽")
        else:
            i.salary="0 ₽"
        if i.price is None or i.price==0 :
            i.price="Не назначена"
    return render(request, "generalreport.html",{"data":data})

@login_required
def workerlist(request):
    data = WorkerInfo.objects.all()
    return render(request, "workerlist.html",{"data":data})

def edit(request, id):
    try:
        data = WorkerInfo.objects.get(id=id)
 
        if request.method == "POST":
            data.name = request.POST.get("name")
            data.price = request.POST.get("price")
            data.save()
            return HttpResponseRedirect("/workerlist")
        else:
            return render(request, "edit.html", {"data": data})
    except WorkerInfo.DoesNotExist:
        return HttpResponseNotFound("<h1>Нет такого рабоника</h1>")
    
def delete(request, id):
    try:
        data = WorkerInfo.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect("/workerlist")
    except WorkerInfo.DoesNotExist:
        return HttpResponseNotFound("<h1>Нет такого рабоника</h1>")
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {'form': form})

def myview(request):
    #user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    #user.last_name = "Lennon"
    #user.save()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseNotFound("<h1>Вы не зарегестрированны </h1>")
    return render(request, "login.html",{"data": data})

