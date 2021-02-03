from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
""" 
Categories
    --Add Category
    --Add Class
"""

# title - title_2 - cover - body - body_2
class Category(models.Model):
    title = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='categories/category/')
    brief = models.TextField(max_length=250)
    body = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    body_2 = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
        ])
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=160,blank=True)
    active = models.BooleanField(default=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title_2)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.title 


# title - title_2 - cover - body - body_2
class Class(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='categories/class/')
    brief = models.TextField(max_length=250)
    body = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    body_2 = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=160,blank=True)
    active = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title_2)
        super(Class,self).save(*args,**kwargs)

    def __str__(self):
        return ( str(self.category) + ", " + str(self.title) )

# cover
class Cover(models.Model):
    cover = models.ImageField(upload_to='categories/cover/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "cover_" + str(self.id)