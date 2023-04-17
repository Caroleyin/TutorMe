from django.contrib import admin
from .models import AppUser, StudentProfile,Course

admin.site.register(AppUser)
admin.site.register(StudentProfile)
admin.site.register(Course)