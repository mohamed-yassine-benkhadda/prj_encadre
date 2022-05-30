from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate,logout
from django.contrib.auth.models import User
import http.client, urllib.parse
from .models import *
import json
import requests

# Create your views here.

def update_user():
    sql_admin = "select * from auth_user where is_superuser = 1"
    admin_user = User.objects.raw(sql_admin)
    for user in admin_user:
        sql = "select * from admin where id_utilisateur = " + str(user.id)
        if len(Admin.objects.raw(sql)) == 0:
            admin = Admin(id_utilisateur= user.id, mail= user.username, tel="")
            admin.save()
    sql_tech = "select * from auth_user where is_staff = 1 and is_superuser = 0"
    tech_user = User.objects.raw(sql_tech)
    for user in tech_user:
        sql = "select * from admin where id_utilisateur = " + str(user.id)
        if len(Admin.objects.raw(sql)) == 0:
            admin = Technicien(id_utilisateur= user.id, mail= user.username, tel="")
            admin.save()


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

def carte(request):
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
            s+= " and public = 'Prive'"
        else :
            s+= " and public = 'Public'"

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

    switch = {1 : "Yes", 0: "No"}
    
    for zone in zones:
        if zone.lat == None:
            zone.lat = extract_lat_lng(zone.nom)[1]
            zone.save()
        if zone.lon == None:
            zone.lon = extract_lat_lng(zone.nom)[0]
            zone.save()
        
        if zone.image != None :
            zone.image = 'Zone/' + (str(zone.image)).split("/")[1]

        if zone.public == "Prive" :
            zone.public = "Private"
            
        zone.camping = switch.get(zone.camping)
        zone.manger = switch.get(zone.manger)
        zone.picnic = switch.get(zone.picnic)
        
    if len(zones) == 0:
        z = {
            "lon" : -6.843613,
            "lat" : 34.007054
        }
    else :
        z = {
            "lon" : zones[0].lon,
            "lat" : zones[0].lat
        }
    return render(request,'carte.html',{
        "zones" : zones,
        "z_lon" : z["lon"],
        "z_lat" : z["lat"],
        "l_zone" : len(zones),
    })

def accueil(request):
    parameters = request.POST
    raws=[
        "select * from zone where 1 limit 3 "
    ]
    zones = Zone.objects.raw(raws[0])
    
    print(raws)
    
    switch = {1 : "Yes", 0: "No"}
    
    
    for zone in zones:
        if zone.lat == None:
            zone.lat = extract_lat_lng(zone.nom)[1]
            zone.save()
        if zone.lon == None:
            zone.lon = extract_lat_lng(zone.nom)[0]
            zone.save()
        
        if zone.image != None :
            zone.image = 'Zone/' + (str(zone.image)).split("/")[1]
        
        if zone.public == "Prive" :
            zone.public = "Private"
            
        zone.camping = switch.get(zone.camping)
        zone.manger = switch.get(zone.manger)
        zone.picnic = switch.get(zone.picnic)
    
    return render(request,'accueil.html',{
        "zones" : zones,
    })

def login_view(request):
    update_user()
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'login.html')

def irrigation(request):
    parameters = request.GET
    zone_id = parameters.get('id')
    zones_list = []
    
    raws=[
        "select pz.id,z.lat as lat,z.lon as lon,p.nom as pnom,p.description as pdescription,pz.dernier_arr as der,pz.prochain_arr as pr from zone z join plante p join plantezone pz on pz.id_zone = z.id and pz.id_plante = p.id where z.id = "+str(zone_id)
    ]
    zones = Zone.objects.raw(raws[0])
    lat = zones[0].lat
    lon = zones[0].lon
    x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=dc3354e8258d3f877c9a8ed8b0ed962b')
    data = x.json()
    temperature = data["main"]["feels_like"] - 273.15
    temperature_min = data["main"]["temp_min"] - 273.15
    temperature_max = data["main"]["temp_max"] - 273.15
    wind_speed = data["wind"]["speed"]
    wind_dir = data["wind"]["deg"]
    descr = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    clouds = data["clouds"]["all"]
    icon_url = "http://openweathermap.org/img/wn/" + icon + ".png"
    for zone in zones:
        zones_list.append(
            {
                "nom" : zone.pnom,
                "description" : zone.pdescription,
                "der" : zone.der,
                "pr" : zone.pr,
                "temperature" : "{:.2f}".format(temperature),
                "temperature_min" : "{:.2f}".format(temperature_min),
                "temperature_max" : "{:.2f}".format(temperature_max),
                "wind_speed" : "{:.2f}".format(wind_speed),
                "wind_dir" : wind_dir,
                "icon_url" : icon_url,
                "descr" : descr,
                "pressure" : pressure,
                "humidity" : humidity,
                "clouds" : clouds,
            }
        )        
    descr = descr.capitalize()
    return render(request,'irrigation.html',{
        'zones':zones,
        "zones_list": zones_list,
        "zone0" : zones[0],
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
            user.save()
            user_1 = Utilisateur(id_utilisateur= user.id, mail= user.username, tel="")
            user_1.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def employee(request):
    return render(request,'employee.html')

def demands(request):
    parameters = request.GET
    id_demande = parameters.get('id')
    op = parameters.get('op')
    if op == "0":
        sql = "delete from demande where id = "+ str(id_demande)
        Demande.objects.raw(sql)[0]
        return redirect('demands')
    elif op == "1":
        sql = "select * from demande where id = "+ str(id_demande)
        d = Demande.objects.raw(sql)[0]
        d.status = 1
        d.save()
        return redirect('demands')
    id_user = request.user.id
    if id_user == None:
        return redirect('login')
    raws=[
        "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_user),
        "select * from demande d join auth_user u where u.id = d.id_utilisateur"
    ]
    users = Admin.objects.raw(raws[0])
    if len(users) == 0:
        return redirect('login')
    demandes = Demande.objects.raw(raws[1])
    return render(request,'demandes.html',{'demandes':demandes})

def green_spaces(request):
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
            
    return render(request,'green-spaces.html',{"zones" : zones})

def green_spaces_plants(request) :
    return render(request,'green-spaces-plants.html')

def green_spaces_add(request):
    id_utilisateur = request.user.id
    sql1 = "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    users = Admin.objects.raw(sql1)
    if len(users) == 0:
        return redirect('login')
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        size = request.POST.get("size")
        public = request.POST.get("public")
        price = request.POST.get("price")
        picnic = request.POST.get("picnic")
        camping = request.POST.get("camping")
        eating = request.POST.get("eating")
        description = request.POST.get("description")
        image = request.POST.get("image")
        sql = f"INSERT INTO `zone`(`nom`, `adresse`, `superficie`, `public`, `prix`, `id_utilisateur`, `picnic`, `camping`, `image`, `description`, `manger`) VALUES ({name},{address},{size},{public},{price},{id_utilisateur},{picnic},{camping},{image},{description},{eating})"
        Zone.objects.raw(sql)
        return redirect('green-spaces')
    return render(request,'green-spaces-add.html')

def green_spaces_edit(request):
    id_utilisateur = request.user.id
    sql1 = "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    users = Admin.objects.raw(sql1)
    if len(users) == 0:
        return redirect('login')
    if request.method == "GET":
        id_zone = request.GET.get("id")
    else :
        return redirect('green-spaces')
    sql2 = "select * from zone where 1 and id = " + str(id_zone)
    zones = Zone.objects.raw(sql2)[0]
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        size = request.POST.get("size")
        public = request.POST.get("public")
        price = request.POST.get("price")
        picnic = request.POST.get("picnic")
        camping = request.POST.get("camping")
        eating = request.POST.get("eating")
        description = request.POST.get("description")
        image = request.POST.get("image")
        sql = f"update zone set nom = \"{name}\", adresse=\"{address}\",superficie={size} ,public={public}, prix={price}, picnic={picnic}, camping={camping}, image=\"{image}\", manger={eating}, description=\"{description}\",id_utilisateur = {id_utilisateur} where id = {id_zone}"
        Zone.objects.raw(sql)
        return redirect('green-spaces')
    return render(request,'green-spaces-edit.html',{"zones" : zones})

def citizen_green_spaces(request):
    
    return render(request,'citizen-green-spaces.html')

def citizen_private_form(request):
    return render(request,'citizen-private-form.html')

def citizen_plants_form(request):
    return render(request,'citizen-plants-form.html')