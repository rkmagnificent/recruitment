from django.db import models


class ApplicantsDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255)
    applied_position = models.CharField(max_length=50)
    terms_and_conditions = models.BooleanField(default=False)
