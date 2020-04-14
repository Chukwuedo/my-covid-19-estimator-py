from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('', views.welcome),
    path('v1/on-covid-19', views.processInput),
    path('v1/on-covid-19/json', views.processInput)
]