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
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)


class Resumes(models.Model):
    applicant = models.ForeignKey(ApplicantsDetails, on_delete=models.CASCADE)
    resume_path = models.FileField(upload_to='documents/')
    uploaded_on = models.DateTimeField(auto_now_add=True, null=True)


class ApplicationStatus(models.Model):
    applicant = models.ForeignKey(ApplicantsDetails, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    updated_on = models.DateTimeField(auto_now=True, null=True)
