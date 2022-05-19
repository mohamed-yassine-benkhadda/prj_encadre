from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)

class Technicien(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    department = models.CharField(max_length=40)

class Admin(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)

class Tache(models.Model):
    id_emp = models.IntegerField()
    id_tech = models.IntegerField()
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField()

class Zone(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=200)
    superficie = models.IntegerField()
    public = models.BooleanField()
    prix = models.BooleanField()
    id_utilisateur = models.IntegerField()
    picnic = models.BooleanField()
    camping = models.BooleanField()
    image = models.ImageField()

class Plante(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField()
    besoin_eau = models.IntegerField()
    image = models.ImageField()

class PlanteZone(models.Model):
    id_zone = models.IntegerField()
    id_plante = models.IntegerField()
    dernier_arr = models.DateTimeField()
    prochain_arr = models.DateTimeField()

class TechnicienZone(models.Model):
    id_zone = models.IntegerField()
    id_emp = models.IntegerField()
    id_resp = models.IntegerField()