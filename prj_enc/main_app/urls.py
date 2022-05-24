from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('irrigation', views.irrigation, name='irrigation'),
    path('demands', views.demands, name='demands'),
    path('employee', views.employee, name='employee'),
    path('green-spaces', views.green_spaces, name='green_spaces'),
    path('citizen-green-spaces', views.citizen_green_spaces, name='citizen_green_spaces'),
    path('citizen-private-form', views.citizen_private_form, name='citizen_private_form'),
    path('citizen-plants-form', views.citizen_plants_form, name='citizen_plants_form'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)