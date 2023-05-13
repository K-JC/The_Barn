from django.shortcuts import render
from django.views import generic

from .models import guest_booking


# Restaurant home page class
class Home (generic.ListView):
    model = guest_booking
    template_name = 'base.html'