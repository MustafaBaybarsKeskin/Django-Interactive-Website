from django.contrib import admin
from .models import Article,Comment

admin.site.register(Comment)
@admin.register(Article)    # bu işlem direkt admin.register."" seklinde de yapilabilirdi.
class ArticleAdmin(admin.ModelAdmin):   
    
    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title","content"]

    list_filter = ["created_date"]

    class Meta: #class içinde meta seklinde class olusturabilme django'da mümkün
        model = Article


