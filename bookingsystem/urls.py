# URLS for booking system
from django.urls import path
from . import views

urlpatterns = [
    # home url
    path('', views.Home.as_view(), name='home'),
    # Booking url
    path('make_booking/', views.MakeBooking.as_view(), name='make_booking'),
    # Menu url
    path('menu/', views.Menu.as_view(), name='menu'),
    # thankyou url
    path('thankyou/', views.Thankyou.as_view(), name='thankyou'),
    # view Booking url
    path('my_booking/', views.ViewBooking.as_view(), name='my_booking'),
    # Edit Booking url
    path('edit_booking/', views.BookingEdit.as_view(), name='edit_booking'),
    # Delete Booking url
    path('delete_booking/', views.BookingDelete.as_view(), name='delete_booking'),
]
