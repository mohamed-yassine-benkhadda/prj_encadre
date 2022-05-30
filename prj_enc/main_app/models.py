from django.db import models

# Create your models here.

choix_demande = (
    ('Arroser','Arroser'),
    ('Planter','Planter')
)

choix_public = (
    ('Public','Public'),
    ('Prive','Prive')
)

class Utilisateur(models.Model):
    id_utilisateur = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)

    class Meta:
        db_table = "Utilisateur"

class Technicien(models.Model):
    id_utilisateur = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    department = models.CharField(max_length=40,blank=True,null=True)

    class Meta:
        db_table = "Technicien"

class Admin(models.Model):
    id_utilisateur = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)

    class Meta:
        db_table = "Admin"

class Tache(models.Model):
    id_admin = models.IntegerField()
    id_tech = models.IntegerField()
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField()

    class Meta:
        db_table = "Tache"

class Zone(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=200)
    superficie = models.IntegerField()
    public = models.CharField(choices=choix_public,max_length=50)
    prix = models.IntegerField(blank=True,null=True)
    id_utilisateur = models.IntegerField(blank=True,null=True)
    picnic = models.BooleanField()
    camping = models.BooleanField()
    manger = models.BooleanField(default=False)
    lat = models.FloatField(blank=True,null=True)
    lon = models.FloatField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='prj_enc/main_app/static/Zone')

    class Meta:
        db_table = "Zone"

class Plante(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        db_table = "Plante"

class PlanteZone(models.Model):
    id_zone = models.IntegerField()
    id_plante = models.IntegerField()
    dernier_arr = models.DateTimeField()
    prochain_arr = models.DateTimeField()

    class Meta:
        db_table = "PlanteZone"

class TechnicienZone(models.Model):
    id_zone = models.IntegerField()
    id_tech = models.IntegerField()
    id_resp = models.IntegerField()

    class Meta:
        db_table = "TechnicienZone"

class Demande(models.Model):
    id_utilisateur = models.IntegerField()
    id_admin = models.IntegerField()
    type_demande = models.CharField(choices=choix_demande,max_length=50)
    description = models.TextField()
    jour = models.DateTimeField()
    adresse = models.CharField(max_length=200)
    status = models.IntegerField()

    class Meta:
        db_table = "Demande"
