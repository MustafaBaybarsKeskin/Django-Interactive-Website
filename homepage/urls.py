from django.urls import path
from . import views

#127.0.0.1:8000/movies
#127.0.0.1:8000/movies/2
#127.0.0.1:8000/movies/search

urlpatterns = [
    path('', views.index, name = 'homepage'),#boş sayfa geçdiğinde index geçsin
    path('<int:pk>', views.detail, name = 'detail'),
    path('search', views.search, name = 'search'),
    path('/blog', views.bindex, name = 'blogpage'),
    path('/blog/<int:pk>', views.bdetail, name = 'bdetail'),
    path('/hakkımızda', views.hakkımızda, name = 'hakkımızda'),
    path('/yazılım', views.ycategory, name = 'ycategory'),
    path('/genel', views.gcategory, name = 'gcategory'),
    path('/eglence', views.egcategory, name = 'egcategory'),
    path('/elektronik', views.elcategory, name = 'elcategory'),
    
]