from django import forms
from .models import guest_booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = guest_booking
        fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email',]

    
