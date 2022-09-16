from django.db import models

# Create your models here.


class Users(models.Model):
    uid = models.CharField(max_length=200 ,null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    avatar = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    social_insurance_number = models.TextField(null=True, blank=True)
    date_of_birth = models.CharField(max_length=255, null=True, blank=True)
 