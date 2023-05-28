from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import guest_booking
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Restaurant home page class, renders the page in the browser


class Home (generic.ListView):
    model = guest_booking
    template_name = 'index.html'


# The get request returns the template as above
def get(self, request):
    return render(request, 'base.html')


# This class will allow the user to create their booking

class MakeBooking(generic.CreateView):
    model = guest_booking
    template_name = 'make_booking.html'
    fields = (['guest', 'day', 'time', 'first_name', 'last_name', 'email'])
    success_url = '/thankyou/'
    
    def booking(self, form):
        booking.is_valid()
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return render(request, 'my_booking.html') 


# This class will allow for the user to edit a booking

# FIX BUG TO EDIT
class BookingEdit(generic.UpdateView):
    model = guest_booking
    template_name = 'edit_booking.html'
    fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email']
    
    def get(self, request):
        return render(request, 'edit_booking.html')


# This class will allow for the user to delete their booking 
# FIX BUG TO DELETE
class BookingDelete(generic.DeleteView):
    model = guest_booking
    template_name = 'delete_booking.html'

    def get(self, request):
        return render(request, 'delete_booking.html')

# Thic class will allow the user to view their bookings


class ViewBooking(generic.ListView):
    model = guest_booking()
    template_name = 'my_booking.html'

    def get(self, request):
        return render(request, 'my_booking.html')


# class allowing menu page to be rendered in the browser 


class Menu(generic.DetailView):
    def get(self, request):
        return render(request, 'menu.html')

# class for the thank you page to be rendered in the browser


class Thankyou(generic.DetailView):
    def get(self, request):
        return render(request, 'thankyou.html')
