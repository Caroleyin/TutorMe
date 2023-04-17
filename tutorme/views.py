from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from schedule_builder.models import Requests
from django.http import JsonResponse

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

class StudentProfileView(generic.ListView):
    template_name = 'tutorme/studentprofile.html'
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

def userpage(request):
	user_form = CustomSignupForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="tutorme/studentprofile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })

def all_requests(request):
    # all_requests = Requests.objects.all()
    all_requests = Requests.objects.filter(tutor_id=request.user.id) | Requests.objects.filter(student_id=request.user.id)
    out = []                                                                                                             
    for req in all_requests:                                                                          
        out.append({                                                                                            
            'start': req.start_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': req.end_time.strftime("%m/%d/%Y, %H:%M:%S"),      
            'student': req.student_id,
            'tutor': req.tutor_id,
            'accepted': req.accepted,
        })                                                                                                                                                                                                                  
    return JsonResponse(out, safe=False)