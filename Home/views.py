from django.shortcuts import render
from Categories.views import Category
from .models import Cover, Opinion, Welcome
from Events.models import Event
from .forms import EmailForm
# Create your views here.

def home(request):
    category_list = Category.objects.filter(active=True)
    categories_last = Category.objects.filter(active=True).order_by('-id')[0:3]
    events_list = Event.objects.filter(active=True).order_by('-id')[0:3]
    coveres = Cover.objects.filter(active=True)
    Opinions = Opinion.objects.all()
    welcome = Welcome.objects.filter(active=True).latest('id')
    if request.method == 'POST':
        pass
    else:
        form = EmailForm()
    context = {
        'categories' : category_list,
        'categories_last' : categories_last,
        'events' : events_list,
        'coveres' : coveres,
        'Opinions' : Opinions,
        'welcome' : welcome,
        'form' : form
    }
    return render(request,'home.html',context)

# def base(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = EmailForm()
#     context = {
#         'form' : form
#     }
#     return render(request,'base.html',context)