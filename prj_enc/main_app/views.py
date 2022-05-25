from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate,logout
from django.contrib.auth.models import User
import http.client, urllib.parse
from .models import *
import json
import requests
import os

# Create your views here.

def extract_lat_lng(c):
    conn = http.client.HTTPConnection('api.positionstack.com')
    params = urllib.parse.urlencode({
        'access_key': '79909e3e1f80bbd6876feeb042bbf395',
        'query': c,
        'limit': 1,
        })
    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    db = json.load(res)
    lat = db['data'][0]['latitude']
    lng = db['data'][0]['longitude']   
    return [lat,lng]

def home(request):
    print(request.GET)
    parameters = request.GET
    search = parameters.get('search')
    eat = parameters.get('eat')
    public = parameters.get('public')
    picnic = parameters.get('picnic')
    camping = parameters.get('camping')
    s = ""
    if search != "" and search != None:
        search_list = search.split(" ")
        s+= f" and adresse like \"%%{search_list[0]}%%\" or nom like \"%%{search_list[0]}%%\""
        for search_item in search_list[1:]:
            s+= f" or adresse like \"%%{search_item}%%\" or nom like \"%%{search_item}%%\""

    if eat != None:
        if eat == '':
            s+= " and manger = 0"
        else :
            s+= " and manger = 1"

    if public != None:
        if public == '':
            s+= " and public = prive"
        else :
            s+= " and public = Public"

    if picnic != None:
        if picnic == '':
            s+= " and picnic = 0"
        else :
            s+= " and picnic = 1"

    if camping != None:
        if camping == '':
            s+= " and camping = 0"
        else :
            s+= " and camping = 1"
    
    raws=[
        "select * from zone where 1 " + s
    ]
    zones = Zone.objects.raw(raws[0])
    for zone in zones:
        if zone.lat == None:
            zone.lat = extract_lat_lng(zone.nom)[1]
            zone.save()
        if zone.lon == None:
            zone.lon = extract_lat_lng(zone.nom)[0]
            zone.save()
    
    return render(request,'index.html',{
        "zones" : zones,
        "zone0" : zones[0]
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'login.html')

def irrigation(request):
    x = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Rabat&appid=dc3354e8258d3f877c9a8ed8b0ed962b')
    data = x.json()
    temperature = data["main"]["feels_like"]-273.15
    raws=[
        "select * from zone where 1 "
    ]
    zones = Zone.objects.raw(raws[0])
    for zone in zones:
        if zone.lat == None:
            zone.lat = extract_lat_lng(zone.nom)[1]
            zone.save()
        if zone.lon == None:
            zone.lon = extract_lat_lng(zone.nom)[0]
            zone.save()
    return render(request,'irrigation.html',{
        'zones':zones,
        "zone0" : zones[0],
        "temperature" : round(temperature),
    })

def register(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            user = User.objects.create_user(username, username, password)
            user.is_staff = True
            user.save()
            return redirect('home')
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def employee(request):
    return render(request,'employee.html')

def demands(request):
    return render(request,'demandes.html')

def green_spaces(request):
    return render(request,'green-spaces.html')

def green_spaces_add(request):
    return render(request,'green-spaces-add.html')

def green_spaces_edit(request):
    return render(request,'green-spaces-edit.html')

def citizen_green_spaces(request):
    return render(request,'citizen-green-spaces.html')

def citizen_private_form(request):
    return render(request,'citizen-private-form.html')

def citizen_plants_form(request):
    return render(request,'citizen-plants-form.html')