from django.contrib import admin
from django.urls import path
from gundem import views

app_name = "gundem"

urlpatterns = [

    path('dashboard/',views.dashboard, name = "dashboard"),
    path('gundemekle/',views.gundemEkle, name = "gundemekle"),
    path('gundem/<int:id>',views.detail, name = "detail"),
    path('update/<int:id>/',views.gundemGuncelle, name = "guncelle"),
    path('delete/<int:id>/',views.gundemSil, name = "sil"),
    path('',views.gundemler, name = "gundemler"),
    path('comment/<int:id>',views.addComment,name = "comment"),


    
]