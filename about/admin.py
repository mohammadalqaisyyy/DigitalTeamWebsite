from django.contrib import admin
from .models import About, Cover

# Register your models here.

class AboutAdmin (admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']
    search_fields = ['title']

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']

admin.site.register(About,AboutAdmin)
admin.site.register(Cover,CoverAdmin)