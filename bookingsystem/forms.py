from django import forms
from .models import guest_booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = guest_booking
        fields = ['guest', 'day', 'time', 'first_name', 'last_name', 'email',]


    guest = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )
    day = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )
    time = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )
    first_name = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )
    last_name = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )
    email = forms.CharField(label='Guest Name', required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Guest Name'}),
    )