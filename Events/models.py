from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

months=(
    ('يناير','يناير'),
    ('فبراير','فبراير'),
    ('مارس','مارس'),
    ('ابريل','ابريل'),
    ('مايو','مايو'),
    ('يونيو','يونيو'),
    ('يوليو','يوليو'),
    ('اغسطس','اغسطس'),
    ('سبتمبر','سبتمبر'),
    ('أكتوبر','أكتوبر'),
    ('نوفيمبر','نوفيمبر'),
    ('ديسمبر','ديسمبر'),
)

Day=(
    ('01','01'),
    ('02','02'),
    ('03','03'),
    ('04','04'),
    ('05','05'),
    ('06','06'),
    ('07','07'),
    ('08','08'),
    ('09','09'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31')
)

class Event(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='events/event/')
    body = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    location = models.CharField(max_length=100)
    Organized_by = models.CharField(max_length=100)
    day = models.CharField(max_length=2, choices=Day)
    month = models.CharField(max_length=15, choices=months)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Cover(models.Model):
    cover = models.ImageField(upload_to='events/cover/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "cover_" + str(self.id)