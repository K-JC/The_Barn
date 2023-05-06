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