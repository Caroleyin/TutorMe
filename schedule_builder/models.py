from django.db import models

from tutorme.models import AppUser
 
# Create your models here.
class Schedule(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
	    return self.user.pk

class Events(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    # tutor = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=None)

class Requests(models.Model):
    event_title = models.CharField(max_length=255,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    # student_name = models.CharField(max_length=255,null=True,blank=True)
    student_id = models.CharField(max_length=255,null=True,blank=True)
    tutor_id = models.CharField(max_length=255,null=True,blank=True)
    accepted = models.BooleanField(default=False)
