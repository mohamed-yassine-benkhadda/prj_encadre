from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.accueil, name="home"),
    path('about', views.about, name='about'),
    path('carte', views.carte, name='carte'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('irrigation', views.irrigation, name='irrigation'),
    path('demands', views.demands, name='demands'),
    path('zone', views.zone, name='zone'),
    path('plante', views.plante, name='plante'),
    path('green-spaces', views.green_spaces, name='green_spaces'),
    path('green-spaces-plants', views.green_spaces_plants, name='green_spaces_plants'),
    path('green-spaces-add', views.green_spaces_add, name='green_spaces_add'),
    path('green-spaces-edit', views.green_spaces_edit, name='green_spaces_edit'),
    path('citizen-green-spaces', views.citizen_green_spaces, name='citizen_green_spaces'),
    path('citizen-private-form', views.citizen_private_form, name='citizen_private_form'),
    path('citizen-plants-form', views.citizen_plants_form, name='citizen_plants_form'), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)