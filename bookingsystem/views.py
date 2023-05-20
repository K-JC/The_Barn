from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import guest_booking


# Restaurant home page class, renders the page in the browser
class Home (generic.ListView):
    model = guest_booking
    template_name = 'index.html'


# The get request returns the template as above
def get(self, request):
    return render(request, 'base.html')