from django.shortcuts import render,redirect
from django.http import HttpResponse
import os

# Create your views here.

def home(request):
    print(os.listdir("main_app"))
    return render(request,'index.html')

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
