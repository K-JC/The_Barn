from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

PICK_TIME = (
    ('12:00 PM', '12:00 PM'),
    ('1:00 PM', '1:00 PM'),
    ('2:00 PM', '2:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('4:00 PM', '4:00 PM'),
    ('5:00 PM', '5:00 PM'),
    ('6:00 PM', '6:00 PM'),
    ('7:00 PM', '7:00 PM'),
    ('8:00 PM', '8:00 PM'),
    ('9:00 PM', '9:00 PM'),
    ('10:00 PM', '10:00 PM'),
)

PICK_GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)

# booking model with CRUD functionality

class guest_booking (models.Model):
    guest = models.CharField(max_length=10, choices=PICK_GUESTS)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=PICK_TIME) # 10
    f_name = models.CharField(max_length=100, default="")
    l_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #return a string representation of an object
    def __str__(self):
        return f"""Name: {self.f_name} {self.l_name} | Guest: {self.guest} | Day: {self.day} | Time: {self.time}"""