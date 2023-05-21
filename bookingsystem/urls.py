# URLS for booking system
from django.urls import path
from . import views


urlpatterns = [
    # home url
    path('', views.Home.as_view(), name='home'),
    # Booking url
    path('bookingsystem/', views.MakeBooking.as_view(),
         name='make_booking'),
]
