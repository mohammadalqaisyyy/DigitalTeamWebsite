from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
"""
* Home
    - cover +  title
    - sub form
    - say
"""

class Welcome (models.Model):
    main_graph =  RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    title_1 = models.CharField(max_length=100,blank=True)
    graph_1 =  RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    title_2 = models.CharField(max_length=100,blank=True)
    graph_2 =  RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    title_3 = models.CharField(max_length=100,blank=True)
    graph_3 =  RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Cover(models.Model):
    cover = models.ImageField(upload_to='home/cover/')
    title = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "cover_" + str(self.id)+" "+self.title

class Opinion(models.Model):
    his_position = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    opinion =  RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    created = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='home/opinion/',blank=True)
    def __str__(self):
        return self.his_position +" "+ self.name


class Email(models.Model):
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now=True)