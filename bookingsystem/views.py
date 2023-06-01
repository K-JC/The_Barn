from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
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
    fields = (['guest', 'day', 'time', 'first_name', 'last_name', 'email'])
    success_url = '/thankyou/'
    
    def booking_view(request):
        if request.method == 'POST':
            form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking = request.user
            booking = save()
            context['form'] = form
        else:
            return render(request, 'thankyou.html')

# FIX BOOKINGS NOT SHOWING ON MY BOOKING PAGE
class ViewBooking(generic.ListView):
    model = guest_booking()
    template_name = 'my_booking.html'
    fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email']

    def get(self, request):
        bookings = guest_booking.objects.filter(user__in=[request.user])
        context = {'booking': bookings} #defined
        return render(request, 'my_booking.html', context)






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
class BookingDelete(generic.DeleteView):
    model = guest_booking
    template_name = 'delete_booking.html'

    def get(self, request):
        return render(request, 'delete_booking.html')