""" This file contains all the
URLs for the barns booking system
"""

from django.urls import path
from . import views


APP_NAME = "thebarn"

urlpatterns = [
    # home url
    path('', views.Home.as_view(), name='home'),
    # Menu url
    path('menu/', views.Menu.as_view(), name='menu'),
    # thankyou url
    path('thankyou/', views.Thankyou.as_view(), name='thankyou'),
    # Make a Booking url
    path('make_booking/', views.MakeBooking.as_view(), name='make_booking'),
    # view Booking url
    path('my_booking/', views.ViewBooking, name='my_booking'),
    # Edit Booking url
    path('<pk>/edit_booking/', views.BookingEdit.as_view(), name='edit_booking'),
    # Delete Booking url
    path('<pk>/delete_booking/', views.BookingDelete.as_view(), name='delete_booking'),
]