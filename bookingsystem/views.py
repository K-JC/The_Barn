from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import GuestBooking
from .forms import BookingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Restaurant home page class, renders the page in the browser


class Home (generic.ListView):
    model = GuestBooking
    template_name = 'index.html'


# The get request returns the template as above
def get(self, request):
    return render(request, 'base.html')


# class renderes the menu page


class Menu(generic.DetailView):
    def get(self, request):
        return render(request, 'menu.html')

# class renderes the thankyou page


class Thankyou(generic.DetailView):
    def get(self, request):
        return render(request, 'thankyou.html')


""" This class allows the registerd user the ability to create their booking,
will send the user to the thank you page once booking has been completed. Checks the
information thats being entered is valid, then saves to database"""


class MakeBooking(LoginRequiredMixin, generic.CreateView):
    model = GuestBooking
    template_name = 'make_booking.html'
    form_class = BookingForm

    def get_success_url(self):
        return reverse('thankyou')

    def booking_add(self, request):
        if request.method == 'POST':
            if form.is_valid:
                booking = form.save(commit=False)
                booking.user = self.request.user
                booking.save()
            return redirect('thankyou')
        else:
            form = BookingForm()
            context = {'form': form}
            return render(request, 'make_booking.html', context)


# The user can view any bookings they have made via the my_booking page, will be listed
def ViewBooking(request):
    if request.user.is_authenticated:
        bookings = GuestBooking.objects.filter()
        context = {'bookings': bookings}

    return render(request, 'my_booking.html')


""" This class will allow for the user to edit a booking and be redirected to my booking page
only feilds for how many guests, what day and what time can be changed, once valid information has
been entered this is saved to the database"""


class BookingEdit(LoginRequiredMixin, generic.UpdateView):
    model = GuestBooking
    fields = ['guest', 'day', 'time']
    template_name = 'edit_booking.html'
    success_url = '/my_booking/'

# The user can delete their booking, will be redirected to mybooking page


class BookingDelete(LoginRequiredMixin, generic.DeleteView):
    model = GuestBooking
    template_name = 'delete_booking.html'
    success_url = '/my_booking/'
