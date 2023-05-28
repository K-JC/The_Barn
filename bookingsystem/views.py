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
# FIX BOOKINGS NOT SHOWING ON MY BOOKING PAGE
class MakeBooking(generic.CreateView):
    model = guest_booking
    template_name = 'make_booking.html'
    fields = (['guest', 'day', 'time', 'first_name', 'last_name', 'email'])
    success_url = '/thankyou/'
    
    def booking_valid(self, form):
        guest_booking = form.save(commit=False)
        guest_booking.user = self.request.user
        guestbooking.save()
        return render(request, 'my_booking.html') 


# This class will allow for the user to edit a booking

# FIX BUG TO EDIT id path ? or pk?
class BookingEdit(generic.UpdateView, id=id):
    model = guest_booking
    template_name = 'edit_booking.html'
    fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email']

    def booking_data(self, *args, **kwargs):
        context = guest_booking, self.booking_data(*args, **kwargs)
        if edit_booking.is_valid():
            edit_booking.save()
        return context

    def get(self, request):
        return render(request, 'edit_booking.html')


# This class will allow for the user to delete their booking 
# FIX BUG TO DELETE need pk or slug?
class BookingDelete(generic.DeleteView):
    model = guest_booking
    template_name = 'delete_booking.html'

    def get(self, request):
        return render(request, 'delete_booking.html')

# Thic class will allow the user to view their bookings

class ViewBooking(generic.DetailView):
    model = guest_booking()
    template_name = 'my_booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = "MISC"
        return context

    def get(self, request):
        return render(request, 'my_booking.html')



# View the list of bookings made


class ViewBooking(generic.ListView):
    model = guest_booking()
    template_name = 'my_booking.html'

    def get_queryset(self):
        logged_user = self.request.user
        return guest_booking.objects.filter(user=logged_user)

# class allowing menu page to be rendered in the browser 


class Menu(generic.DetailView):
    def get(self, request):
        return render(request, 'menu.html')

# class for the thank you page to be rendered in the browser


class Thankyou(generic.DetailView):
    def get(self, request):
        return render(request, 'thankyou.html')
