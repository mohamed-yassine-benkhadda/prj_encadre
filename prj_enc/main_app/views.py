from django.shortcuts import render,redirect
import os

# Create your views here.

def home(request):
    print(os.listdir("main_app"))
    return render(request,'home.html')
