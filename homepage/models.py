from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Haber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Haber adı')
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(max_length=50, verbose_name='Haber resmi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default= True)
    

    def __str__(self):
        return self.name

   


class BlogPost(models.Model):
    name = models.CharField(max_length=50, verbose_name='Blog Post Adı')
    summary = models.TextField( verbose_name='Blog Post Özeti')
    description = RichTextField(verbose_name='Blog Post Metni')
    image = models.ImageField(max_length=50, verbose_name='Blog Post Resmi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    writername =  models.CharField(max_length=50, verbose_name='Yazar Adı')
    theme = models.CharField(max_length=50, verbose_name='Tema Rengi')
    isPublished = models.BooleanField(default= True)
    category = models.CharField(max_length=50, verbose_name='Blog Post Kategori')
    
    def __str__(self):
        return self.name




        
#bunları bu dosya altındaki admin.py ye kayıt etmeliyiz