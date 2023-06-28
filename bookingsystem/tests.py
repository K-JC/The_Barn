from django.test import TestCase
from bookingsystem.models import GuestBooking
from django.contrib.auth.models import User



class ViewsTesting(TestCase):

    def setUp(self):
        GuestBooking.objects.create(
        guest='4',
        day='2023-10-20',
        time='19:00',
        first_name='Elizabeth',
        last_name='Well',
        email='Liz@email.com',
        )

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_thankyou_view(self):
        response = self.client.get('/thankyou/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thankyou.html', 'base.html')

    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html', 'base.html')

    def test_my_booking_view(self):
        response = self.client.get('/my_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_booking.html', 'base.html')
