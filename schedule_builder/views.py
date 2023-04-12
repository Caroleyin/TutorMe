from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse 
from schedule_builder.models import Events
from tutorme.models import AppUser
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)

		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('schedule_builder:tutor')
	else:
		u_form = UserUpdateForm(instance=request.user)

	context = {
		'u_form': u_form,
	}

	return render(request, 'tutor_base.html', context)

@login_required
def index(request):  
    all_events = Events.objects.filter(tutor = request.user)
    context = {
        "events":all_events,
    }
    return render(request,'schedule_index.html',context)
 
@login_required
def all_events(request):                                                                                                 
    all_events = Events.objects.filter(tutor = request.user)                                                                                    
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
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    tutor = request.user
    newtitle = str(title) + '\n' + 'Hourly Rate: $' + str(tutor.hourly_rate)
    event = Events(name=newtitle, start=start, end=end)
    event.tutor = tutor
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

