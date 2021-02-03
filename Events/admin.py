from django.contrib import admin

# Register your models here.
from .models import Event, Cover

class EventAdmin(admin.ModelAdmin):
    list_filter = ['created','active','year']
    list_display = ['title','created','active']
    search_fields = ['title']

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']


admin.site.register(Event,EventAdmin)
admin.site.register(Cover,CoverAdmin)