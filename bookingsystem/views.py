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



# This class will allow the user to create their booking (bookings are being made)

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
            context = {'form': form}

            return render(request, 'thankyou.html')
       
         

# View bookings made on the my_booking page/ AUTHORISED USER ONLY
#user=request.user (hid all bookings)

def ViewBooking(request): 
    if request.user.is_authenticated:
        form_class = BookingForm
        bookings = guest_booking.objects.filter()
        return render(request, 'my_booking.html', {'bookings': bookings})


# This class will allow for the user to edit a booking
# FIX BUG TO EDIT id path ? or pk?

def BookingEdit(request, booking_id):
    template_name = 'edit_booking.html'
    if request.user.is_authenticated:
        bookings = get_object_or_404(guest_booking, id=booking_id)
        if booking.user == request.user:
            if request.method == 'POST':
                form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('edit_booking.html')
    form = BookingForm(instance=booking)
    context = {'form': form}
    return render(request, 'edit_booking.html', context)



# This class will allow for the user to delete their booking 
# FIX BUG TO DELETE need pk or slug?
def BookingDelete(request):
    if request.user.is_authenticated:
        booking = get_object_or_404(guest_booking, id=booking_id)
        if booking.user == request.user:
            booking.delete()
    return redirect('my_booking.html')