from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate,logout
from django.contrib.auth.models import User
import http.client, urllib.parse
from .models import *
import json
import requests
import datetime
from django.db import connection

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
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
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
        "logged" : logged,
        "mail" : mail,
    })

def accueil(request):
    staff = False
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    parameters = request.POST
    raws=[
        "select * from zone where 1 limit 3 ",
        f"select * from auth_user where id = {request.user.id}"
    ]
    zones = Zone.objects.raw(raws[0])
    if request.user.id != None:
        staff = Admin.objects.raw(raws[1])[0].is_active
        admin = Admin.objects.raw(raws[1])[0].is_superuser
    else:
        admin = False
    
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
        "staff" : staff,
        "admin" : admin,
        "logged" : logged,
        "mail" : mail,
    })

def login_view(request):
    logout(request)
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
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    parameters = request.GET
    zone_id = parameters.get('id')
    try:
        pz = parameters.get('pz')
        sql = f"select * from plantezone where id = {str(pz)}"
        print(sql)
        plantezone = PlanteZone.objects.raw(sql)
        plantezone[0].dernier_arr = datetime.datetime.now().isoformat()
        plantezone[0].status = 1
        plantezone[0].save()
        sql = "delete from tache where status = 1 id_pz = "+ str(pz)
        Tache.objects.delete(sql)[0]
        sql = f"select id_zone as id from PlanteZone where id ="+str(pz)
        id_z=PlanteZone.objects.raw(sql)[0].id_zone
        return redirect('accueil')
    except:
        pass
    if zone_id == None or zone_id=="":
        zone_id = id_z
    zones_list = []
    id_user = request.user.id
    if id_user == None:
        return redirect('login')
    raws=[
        "select * from admin a join auth_user au join technicien t where au.id = t.id_utilisateur or au.id = a.id_utilisateur and au.id = " + str(id_user),
        f"select * from auth_user u where u.id = {request.user.id}"
    ]
    users = Admin.objects.raw(raws[0])
    if len(users) == 0:
        return redirect('login')

    admin = Admin.objects.raw(raws[1])[0].is_superuser
    
    raws=[
        "select z.id as zid,pz.id as id,z.lat as lat,z.lon as lon,p.nom as pnom,p.description as pdescription,pz.dernier_arr as der,pz.prochain_arr as pr,z.id as zoneid from zone z join plante p join plantezone pz on pz.id_zone = z.id and pz.id_plante = p.id where z.id = "+str(zone_id),
        "SELECT * from technicien GROUP BY mail",
        f"select z.id as zid,pz.id as id,z.lat as lat,z.lon as lon,p.nom as pnom,p.description as pdescription,pz.dernier_arr as der,pz.prochain_arr as pr,z.id as zoneid from zone z join plante p join plantezone pz join auth_user au join tache where tache.id_tech=au.id and tache.id_pz=pz.id and pz.id_zone = z.id and pz.id_plante = p.id and au.id = {request.user.id} and pz.id_zone = {str(zone_id)}"
    ]
    print(raws[0])
    zones_tech = PlanteZone.objects.raw(raws[2])
    zones = Zone.objects.raw(raws[0])
    technicien = Technicien.objects.raw(raws[1])
    lat = zones[0].lat
    id = zones[0].id
    lon = zones[0].lon
    s = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=dc3354e8258d3f877c9a8ed8b0ed962b'
    x = requests.get(s)
    data = x.json()
    e_time = datetime.datetime.now() - zones[0].der
    e_time = e_time.total_seconds()/3600
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
        e_time = datetime.datetime.now() - zone.der
        e_time = e_time.total_seconds()/3600
        zones_list.append(
            {
                "id" : zone.id,
                "nom" : zone.pnom,
                "temps" : e_time,
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
    if request.method == "POST":
        parametersPost = request.POST
        tech_id = parametersPost.get('techniciens')
        pz_id = parametersPost.get('plante')
        print(pz_id)
        t = Tache(id_admin=request.user.id,id_tech=tech_id,id_pz=pz_id,description="Arroser la plante",status=0)
        t.save()
    descr = descr.capitalize()
    if admin:
        return render(request,'irrigation.html',{
            'zones':zones,
            "zones_list": zones_list,
            "zones_list0": zones_list[0],
            "zone0" : zones[0],
            "technicien" : technicien,
            "zoneid" : zones[0].zoneid,
            "mail" : mail,
            "logged" : logged,
            })
    return render(request,'irrigation_tech.html',{
            'zones':zones,
            "zones_list": zones_list,
            "zones_tech": zones_tech,
            "zones_list0": zones_list[0],
            "zone0" : zones[0],
            "technicien" : technicien,
            "zoneid" : zones[0].zoneid,
            "mail" : mail,
            "logged" : logged
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
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    return render(request,'about.html',{
        "logged" : logged,
        "mail" : mail
    })

def demands(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    parameters = request.GET
    id_demande = parameters.get('id')
    op = parameters.get('op')
    if op == "0":
        record = Demande.objects.get(id = id_demande)
        record.delete()
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
    return render(request,'demandes.html',{
        'demandes':demandes,
        "logged" : logged,
        "mail" : mail
    })

def green_spaces(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    id_utilisateur = request.user.id
    sql1 = "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    sql2 = "select * from technicien a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    users = Admin.objects.raw(sql1)
    users2 = Admin.objects.raw(sql2)
    if len(users) == 0 and len(users2) == 0 :
        zones = Zone.objects.filter(id_utilisateur = id_utilisateur)
        return render(request,'green-spaces.html',{"zones" : zones})
    raws=[
        f"select * from auth_user u where u.id = {request.user.id}"
    ]
    admin = Admin.objects.raw(raws[0])[0].is_superuser
    raws=[
        "select * from zone where 1 "
    ]
    if request.GET.get("id") != None and request.GET.get("id") != "":
        id = request.GET.get("id")
        record = Zone.objects.get(id = id)
        record.delete()
        return redirect('green_spaces')
    zones = Zone.objects.raw(raws[0])
            
    return render(request,'green-spaces.html',{
        "zones" : zones,
        "logged" : logged,
        "mail" : mail,
        "admin" : admin,
    })

def green_spaces_plants(request) :
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    id_utilisateur = request.user.id
    sql1 = "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    users = Admin.objects.raw(sql1)
    if len(users) == 0:
        return redirect('login')
    zones = Zone.objects.all()
    plantes = Plante.objects.all()
    parameters = request.POST
    zone = parameters.get('zone')
    plante = parameters.get('plante')
    besoin = parameters.get('besoin')
    if zone != None and plante != None and besoin != None:
        pz = PlanteZone(id_zone = zone, id_plante = plante, prochain_arr = besoin,dernier_arr=datetime.datetime.now().isoformat())
        pz.save()
        return redirect('green_spaces')
    return render(request,'green-spaces-plants.html',{
        "zones" : zones,
        "plantes" : plantes,
        "logged" : logged,
        "mail" : mail
    })

def green_spaces_add(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
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
        if picnic == None:
            picnic = False
        if camping == None:
            camping = False
        if eating == None:
            eating = False
        z = Zone(nom=name,adresse=address,superficie=size,public=public,prix=price,picnic=picnic,camping=camping,manger=eating,description=description,image=image)
        z.save()
        return redirect('green_spaces')
    return render(request,'green-spaces-add.html',{
        "logged" : logged,
        "mail" : mail
    })

def green_spaces_edit(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    id_utilisateur = request.user.id
    sql1 = "select * from admin a join auth_user au where au.id = a.id_utilisateur and au.id = " + str(id_utilisateur)
    users = Admin.objects.raw(sql1)
    if len(users) == 0:
        return redirect('login')
    id_zone = request.GET.get("id")
    print(id_zone)
    
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
        if picnic == None:
            picnic = False
        if camping == None:
            camping = False
        if eating == None:
            eating = False
        with connection.cursor() as cursor:
            sql = f"update zone set nom = \"{name}\", adresse=\"{address}\",superficie={size} ,public={public}, prix={price}, picnic={picnic}, camping={camping}, manger={eating}, description=\"{description}\",id_utilisateur = {id_utilisateur} where id = {id_zone}"
            print(sql)
            cursor.execute(sql)
            return redirect('green_spaces')
    return render(request,'green-spaces-edit.html',{
        "zones" : zones,
        "logged" : logged,
        "mail" : mail
    })

def citizen_green_spaces(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    return render(request,'citizen-green-spaces.html',{
        "logged" : logged,
        "mail" : mail
    })

def citizen_private_form(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    
    return render(request,'citizen-private-form.html',{
        "logged" : logged,
        "mail" : mail
    })

def citizen_plants_form(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
        return redirect('login')
    if request.method == "POST":
        type_demande = request.POST.get("type")
        address = request.POST.get("address")
        date = request.POST.get("date")
        description = request.POST.get("description")
        d = Demande(type_demande = type_demande,adresse = address,jour=date,description=description,id_utilisateur	=request.user.id,status=2)
        d.save()
        return redirect("home")
    return render(request,'citizen-plants-form.html',{
        "logged" : logged,
        "mail" : mail
    })

def zone(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
        return redirect('login')
    raws=[
        f"select * from auth_user u where u.id = {request.user.id}"
    ]
    admin = Admin.objects.raw(raws[0])[0].is_superuser
    id = request.GET.get('id')
    zones_list = Zone.objects.filter(id = id)[0]
    if zones_list.image != None :
        zones_list.image = 'Zone/' + (str(zones_list.image)).split("/")[1]
    raws=[
        "select z.id as zid,pz.id as id,z.lat as lat,z.lon as lon,p.nom as pnom,p.image as image,p.description as pdescription,pz.dernier_arr as der,pz.prochain_arr as pr,z.id as zoneid from zone z join plante p join plantezone pz on pz.id_zone = z.id and pz.id_plante = p.id where z.id = "+str(id),
    ]
    print(raws[0])
    zones = Zone.objects.raw(raws[0])
    for zone in zones:
        if zone.image != None :
            zone.image = 'Plante/' + (str(zone.image)).split("/")[1]
    if admin :
        return render(request,'zone-admin.html',{
        "zones": zones,
        "zones_list": zones_list,
        "logged" : logged,
        "mail" : mail
    })    
    return render(request,'zone.html',{
        "zones": zones,
        "zones_list": zones_list,
        "logged" : logged,
        "mail": mail,
    })

def plante(request):
    logged = request.user.id
    if logged != None:
        mail = User.objects.filter(id = logged)[0].username
        print(mail)
    else:
        mail = ""
    parameters = request.POST
    nom = request.POST.get("name")
    description = request.POST.get("description")
    image = request.POST.get("image")
    p = Plante(nom = nom, description = description, image = image)
    return render(request,'plante.html',{
        "logged" : logged,
        "mail" : mail
    })