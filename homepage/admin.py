from django.contrib import admin
from .models import Haber, BlogPost


class HaberAdmin(admin.ModelAdmin):#admin panelindeki haber ekleme kısmında ki başlıklar
    list_display = ('id', 'name', 'created_date', 'isPublished',)
    list_display_links = ('id', 'name')#id ve name ler link olarak gözükecektir
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description')
    list_per_page = 20

# Register your models here.

admin.site.register(Haber, HaberAdmin)
admin.site.register(BlogPost, HaberAdmin)