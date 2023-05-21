from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import guest_booking
from django.views.generic.edit import UpdateView, DeleteView

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

    def success_url(self, request):
        return render(request, 'thankyou.html')


# This class will allow for the user to edit a booking
class BookingEdit(generic.UpdateView):
    model = guest_booking
    template_name = 'edit_booking.html'
    fields = (['guest', 'day', 'time', 'first_name', 'last_name', 'email'])
    success_url = 'bookingsystem/my_booking.html'


# This class will allow for the user to delete their booking
class BookingDelete(generic.DeleteView):
    model = guest_booking
    template_name = 'delete_booking.html'
    success_url = 'bookingsystem/my_booking.html'

# Thic class will allow the user to view their bookings


class ViewBooking(generic.ListView):
    model = guest_booking
    template_name = 'my_booking.html'
    success_url = 'bookingsystem/my_booking.html'
