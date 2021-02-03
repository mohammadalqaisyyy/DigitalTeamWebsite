from django.shortcuts import render
from .models import Event, Cover

# Create your views here.
def all_Events(request):
    event_list = Event.objects.filter(active=True)
    cover = Cover.objects.latest('id')
    print("HERE")
    # cover = Cover.objects.latest('id')
    context = {
        'Events' : event_list,
        'one_cover' : cover,
    }
    return render(request,'event.html',context)