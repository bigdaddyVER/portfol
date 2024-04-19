from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('works', views.works, name="works"),
    path('what', views.what, name="what"),
    
]