from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver #add this
from django.db.models.signals import post_save
from django.contrib import admin

class AppUser(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField("Year", max_length=4, default='', blank=True)
    major = models.CharField("Major(s)/minor(s)", max_length=100, default='', blank=True)
    description = models.TextField("Description", max_length=600, default='', blank=True)
    hourly_rate = models.FloatField(default=0)
    courses = models.ManyToManyField('CourseAsText', blank=True)

class Review(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='review', null=True)
    title_text = models.TextField(default="")
    review_text = models.TextField(default="")
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    def __str__(self):
        return self.review_text
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=10)
    catalog_number = models.CharField(max_length=10)
    course_id = models.CharField(max_length=10)
    is_enrolled = models.BooleanField(default=False)
    meeting_days = models.CharField(max_length=10)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)


class CourseAsText(models.Model):
    title = models.CharField(max_length=100)
