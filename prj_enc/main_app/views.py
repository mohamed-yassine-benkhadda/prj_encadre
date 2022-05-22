from django.shortcuts import render,redirect
<<<<<<< HEAD
from django.contrib.auth import get_user_model,login,authenticate,logout
from .models import *
=======
from django.http import HttpResponse
>>>>>>> 0461fbdcf10010290630b3eaf034367822bc7503
import os

# Create your views here.

def home(request):
    parameters = request.GET
    search = parameters.get('search')
    eat = parameters.get('eat')
    public = parameters.get('public')
    picnic = parameters.get('picnic')
    camping = parameters.get('camping')
    s = ""
    if search != "" and search != None:
        search_list = search.split(" ")
        s+= " and adresse = {search_list[0]} or nom = {search_list[0]}"
        for search_item in search_list[1:]:
            s+= f" or adresse = {search_item} or nom = {search_item}"
    raws=[
        "select * from zone where 1"
    ]
    zones = Zone.objects.raw(raws[0])
    return render(request,'index.html')

<<<<<<< HEAD
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"\n\n\n{user.username}\t{user.password}\n\n\n")
            return redirect('accueil')
    return render(request,'login.html')

def irrigation(request):
    return render(request,'irrigation.html')

def register(request):
    return render(request,'register.html')
=======
def about(request):    
    return HttpResponse('<h1>Not yet available</h1>') 

def login(request):    
    return render(request, 'pages/login.html')

def register(request):    
    return render(request, 'pages/register.html') 

def employee(request):    
    return render(request, 'pages/employee.html') 

def irrigation(request):    
    return render(request, 'pages/irrigation.html') 

def demands(request):    
    return render(request, 'pages/demandes.html') 

def green_spaces(request):    
    return render(request, 'pages/green-spaces.html') 
>>>>>>> 0461fbdcf10010290630b3eaf034367822bc7503
