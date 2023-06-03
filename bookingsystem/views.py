from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import guest_booking
from .forms import BookingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Restaurant home page class, renders the page in the browser


class Home (generic.ListView):
    model = guest_booking
    template_name = 'index.html'


# The get request returns the template as above
def get(self, request):
    return render(request, 'base.html')


# class allowing menu page to be rendered in the browser 


class Menu(generic.DetailView):
    def get(self, request):
        return render(request, 'menu.html')

# class for the thank you page to be rendered in the browser


class Thankyou(generic.DetailView):
    def get(self, request):
        return render(request, 'thankyou.html')



# This class will allow the user to create their booking


class MakeBooking(generic.CreateView):
    model = guest_booking
    template_name = 'make_booking.html'
    form_class = BookingForm
    
    def get_success_url(self):
        return reverse('thankyou')

    def booking_valid(self, request):
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = self.request.user
            booking.save()
            return render(request, 'thankyou.html')
        else:
            context = {'form': form}
            return render(request, 'make_booking.html', context)

# FIX BOOKINGS NOT SHOWING ON MY BOOKING PAGE # booking id?


class ViewBooking(generic.DetailView):
    template_name = 'my_booking.html'
    model = guest_booking
    context = {'booking'}

    def get_object(self, *args, **kwargs):
        logged_user = self.request.user
        return guest_booking.objects.all()
    



# LEAVE THIS TILL AFTER
# This class will allow for the user to edit a booking
# FIX BUG TO EDIT id path ? or pk?
class BookingEdit(generic.UpdateView):
    model = guest_booking
    template_name = 'edit_booking.html'
    fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email']
    def get(self, request):
        return render(request, 'edit_booking.html')


# This class will allow for the user to delete their booking 
# FIX BUG TO DELETE need pk or slug?
class BookingDelete(DeleteView):
    model = guest_booking
    template_name = 'delete_booking.html'
  

    def get(self, request):
        return redirect('my_booking.html')