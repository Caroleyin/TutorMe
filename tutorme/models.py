from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver #add this
from django.db.models.signals import post_save

class AppUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField("Year", max_length=4, default='', blank=True)
    major = models.CharField("Major(s)/minor(s)", max_length=100, default='', blank=True)
    description = models.TextField("Description", max_length=600, default='', blank=True)
    hourly_rate = models.FloatField(default=0)

class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=10)
    catalog_number = models.CharField(max_length=10)
    course_id = models.CharField(max_length=10)
    is_enrolled = models.BooleanField(default=False)
    meeting_days = models.CharField(max_length=10)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)

