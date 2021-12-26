from django.contrib import admin
from django.urls import path
from article import views

app_name = "article"

urlpatterns = [

    path('kontrolpaneli/',views.dashboard, name = "dashboard"),
    path('konuekle/',views.addArticle, name = "addarticle"),
    path('konu/<int:id>',views.detail, name = "detail"),
    path('guncelle/<int:id>/',views.updateArticle, name = "update"),
    path('konusil/<int:id>/',views.deleteArticle, name = "delete"),
    path('',views.articles, name = "articles"),
    path('yorum/<int:id>',views.addComment,name = "comment"),


    
]