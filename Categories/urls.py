from django.urls import path, include
from . import views

urlpatterns = [
    path('Categories/', views.all_category),
    path('Categories/<str:slug>/', views.category),
    path('Class/<str:slug>/', views.Class_one),
]