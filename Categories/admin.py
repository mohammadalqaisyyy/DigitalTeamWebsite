from django.contrib import admin

# Register your models here.
from .models import Category, Class, Cover

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['title','title_2','created','active']
    search_fields = ['title','title_2']

class ClassAdmin(admin.ModelAdmin):
    list_filter = ['category','created','active']
    list_display = ['title','title_2','category','created','active']
    search_fields = ['title','title_2','category']

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Cover,CoverAdmin)