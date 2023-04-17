from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse 
from schedule_builder.models import Events
from tutorme.models import AppUser
from .forms import AddClass
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from schedule_builder.models import Requests
from schedule_builder.models import Schedule
from tutorme.models import StudentProfile


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=TutorProfile.objects.filter(user = request.user).first())

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('schedule_builder:tutor')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=TutorProfile.objects.filter(user = request.user).first())

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'tutor_base.html', context)

@login_required
def index(request, user_id):
    # if the visiting user isn't the the same user as the user whose schedule they're viewing
    if (request.user.id != user_id):
        all_events = Events.objects.filter(schedule=Schedule.objects.get(user = AppUser.objects.get(pk = user_id)))
        context = {
            "tutor_id":user_id,
            "events":all_events,
        }
        return render(request,'student_schedule_index.html',context)

    if not Schedule.objects.filter(user = AppUser.objects.get(pk=request.user.id)):
        s = Schedule(user = AppUser.objects.get(pk=request.user.id)) 
        s.save()

    all_events = Events.objects.filter(schedule=Schedule.objects.get(user = AppUser.objects.get(pk = request.user.id)))
    context = {
        "tutor_id":user_id,
        "events":all_events,
    }
    return render(request,'schedule_index.html',context)
 
@login_required
def all_events(request, user_id):                                                                                                 
    # all_events = Events.objects.filter(tutor = TutorProfile.objects.filter(user = request.user).first())    
    all_events = Events.objects.filter(schedule=Schedule.objects.get(pk = user_id))                                                                                 
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
@login_required
def add_event(request):
    # start = request.GET.get("start", None)
    # end = request.GET.get("end", None)
    # title = request.GET.get("title", None)
    # tutor = StudentProfile.objects.filter(user = request.user).first()
    # newtitle = str(title) + '\n' + 'Hourly Rate: $' + str(tutor.hourly_rate)
    # event = Events(name=newtitle, start=start, end=end)
    # event.tutor = AppUser.objects.filter(user = request.user).first()
    # event.save()
    # data = {}
    # return JsonResponse(data)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    # change name=request.user.id if needed (to the unique identifer)
    event = Events(name=str(title), start=start, end=end, schedule=Schedule.objects.get(user=AppUser.objects.get(pk = request.user.id)))
    event.save()
    data = {}
    return JsonResponse(data)
 
@login_required
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
@login_required
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

@login_required
def request_tutor(request, user_id):
    if request.method == "GET":
        title = request.GET.get("title", None)
        start = request.GET.get("start", None)
        end = request.GET.get("end", None)
        student = request.user.id
        tutor = user_id
        request = Requests(event_title = title, start_time = start, end_time = end, student_id = student, tutor_id = tutor)
        request.save()
        data = {}
        return JsonResponse(data)
        # request_list = Requests.objects.all()
        # return render(request, 'request/list.html', {'comment_list': request_list})