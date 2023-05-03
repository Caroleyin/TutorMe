from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from .models import AppUser
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import AppUser, CourseAsText, Review
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from schedule_builder.models import Requests

import requests
import json

class IndexView(generic.ListView):
    template_name = 'tutorme/index.html'
    context_object_name = 'tutors'
    def get_queryset(self):
        return

class AuthView(generic.ListView):
    template_name = 'tutorme/auth.html'
    def get_queryset(self):
        return

class AboutView(generic.ListView):
    template_name = 'tutorme/about.html'
    def get_queryset(self):
        return

class SearchForTutor(generic.ListView):
    template_name = 'tutorme/searchForTutor.html'
    context_object_name = 'tutors'

    def get_queryset(self):
        course_title = self.request.GET.get('course', '')
        course = CourseAsText.objects.filter(title=course_title).first()
        if course:
            return AppUser.objects.filter(is_tutor=True, courses=course)
        else:
            return None
class StudentView(generic.ListView):
    template_name = 'tutorme/student.html'
    def get_queryset(self):
        return

class TutorAddClassView(generic.ListView):
    template_name = 'tutorme/tutorAddClasses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return self.request.user.courses.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1'
            response = requests.get(url + '&subject=' + request.POST['department-select'] + '&catalog_nbr=' + request.POST['course-number-input'])
            for c in response.json():
                text = c['subject']
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
    
"""
 
class StudentProfileView(generic.CreateView):   
    model = AppUser
    template_name = 'tutorme/studentprofile.html'
    fields = ['first_name', 'last_name', 'year', 'major', 'description']

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
"""

def postComment(request, pk):
    user = get_object_or_404(AppUser, pk=pk)
    if request.method == 'POST':
            user = get_object_or_404(AppUser, pk=pk)
            review = Review(title_text=request.POST['title_field'], review_text=request.POST['comment_field'], user=user)
            review.save()
    return HttpResponseRedirect(reverse('tutorme:post', args=(user.username,)))
    

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('tutorme:profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'tutorme/studentprofile.html', context={'form': form, 'user_id': user.id})
    return render(request, 'tutorme/studentprofile.html')

