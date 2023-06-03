from django import forms
from .models import guest_booking

# Calender Option when booking 
class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):

    class Meta:
        model = guest_booking
        fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email',]
        widgets = {'day': DateInput()}
