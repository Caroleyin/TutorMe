from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import AppUser, CourseAsText
from django.shortcuts import redirect

class IndexView(generic.ListView):
    template_name = 'tutorme/index.html'
    context_object_name = 'tutors'
    def get_queryset(self):
        return

class AuthView(generic.ListView):
    template_name = 'tutorme/auth.html'
    def get_queryset(self):
        return
    
class StudentView(generic.ListView):
    template_name = 'tutorme/student.html'
    def get_queryset(self):
        return
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            text = request.body.decode('utf-8')

            text = text[93:]
            ampIndex = text.find('&')
            text = text[:ampIndex]
            text = text.replace('+', ' ')
            print(text)
            if text:
                user_profile = request.user

                course = CourseAsText.objects.filter(title=text).first()
                if (course is None):
                    course = CourseAsText.objects.create(title=text)

                findClass = user_profile.courses.filter(pk=course.pk).first()
                if (findClass is None):
                    findClass = course

                user_profile.courses.add(findClass)
                user_profile.save()

                return redirect('/tutorme/student/')
        return JsonResponse({'status': 'error'})

class StudentProfileView(generic.ListView):
    template_name = 'tutorme/profile.html'
    def get_queryset(self):
        return

class CourseSearchView(generic.ListView):
    template_name = 'tutorme/course_search.html'
    def get_queryset(self):
        return

class AboutView(generic.ListView):
    template_name = 'tutorme/about.html'
    def get_queryset(self):
        return