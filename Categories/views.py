from django.shortcuts import render
from .models import Category, Class, Cover

# Create your views here.

# Categories
def all_category(request):
    category_list = Category.objects.filter(active=True)
    cover = Cover.objects.latest('id')
    context = {
        'categories' : category_list,
        'one_cover' : cover,
    }
    return render(request,'categories.html',context)

# Category
def category(request, slug):
    category_one = Category.objects.get(slug=slug)
    category_list = Category.objects.filter(active=True)
    classes = Class.objects.filter(category=category_one,active=True)
    context = {
        'category' : category_one,
        'categories' : category_list,
        'classes': classes
    }
    return render(request,'category.html',context)

def Class_one(request, slug):
    class_one = Class.objects.get(slug=slug)
    category_list = Category.objects.filter(active=True)
    context = {
        'class': class_one,
        'categories' : category_list,
    }
    return render(request,'class.html',context)