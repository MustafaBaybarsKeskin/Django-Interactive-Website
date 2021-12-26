from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Gundem(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField(verbose_name= "İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
    
class Comment(models.Model):
    gundem = models.ForeignKey(Gundem,on_delete = models.CASCADE,verbose_name = "Konu Başlığı",related_name="comments")
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="author")
    comment_content = RichTextField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']