from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('form/', views.form, name ="form"),
    
]