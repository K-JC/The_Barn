# URLS for booking system 
from django.urls import path
from . import views


urlpatterns = [
    # home url
    path('', views.Home.as_view(), name='home'),
    #
]