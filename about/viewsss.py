from django.shortcuts import render
from .models import About, Cover

# Create your views here.

def about_one(request):
    about_last = About.objects.filter(active=True)
    cover = Cover.objects.latest('id')
    context = {
        'about' : about_last,
        'one_cover' : cover,
    }
    return render(request,'about.html',context)