from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name="accueil"),
    path('login', views.login_view, name="login"),
    path('irrigation', views.irrigation, name="irrigation"),
    path('register', views.register, name="register"),
=======
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('irrigation/', views.irrigation, name='irrigation'),
    path('demands/', views.demands, name='demands'),
    path('employee/', views.employee, name='employee'),
    path('green-spaces/', views.green_spaces, name='green_spaces'),
>>>>>>> 0461fbdcf10010290630b3eaf034367822bc7503
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)