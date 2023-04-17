from django.db import models

from tutorme.models import AppUser
 
# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    tutor = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=None)
