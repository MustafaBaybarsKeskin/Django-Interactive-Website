from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Haber, BlogPost

# Create your views here.
def index(request):
    habers = Haber.objects.all().order_by('-created_date',)[5::]
    posts = Haber.objects.filter().order_by('-created_date')[0:1]
    postsiki = Haber.objects.filter().order_by('-created_date')[1:5]
    mbpost = BlogPost.objects.all().order_by('-created_date',)[0:6]

    context = {
        'habers': habers,
        'posts': posts,
        'postsiki' : postsiki,
        'mbpost' : mbpost,
        
        
    }
    
    return render(request, 'homepage/list.html', context)

def detail(request, pk):
    haber = get_object_or_404(Haber, pk = pk)
    
    context = {
        'haber':haber,  
    }
    return render(request, 'homepage/detail.html', context)


    
def hakkımızda(request):

    return render(request, 'homepage/hakkımızda.html')
    

def search(request):
    return render(request, 'search/list.html')


def bindex(request):
    bpost = BlogPost.objects.all().order_by('-created_date',)
    bhabers = Haber.objects.all().order_by('-created_date',)[0:5]
    context = {
        'bpost': bpost,
        'bhabers' : bhabers,
    }
    return render(request, 'homepage/bloglist.html', context)

    
def bdetail(request, pk):
    bpos = get_object_or_404(BlogPost, pk = pk)
    
    context = {
        'bpos':bpos,  
    }
    return render(request, 'homepage/blogdetail.html', context)

def ycategory(request):
    bpost = BlogPost.objects.all().order_by('-created_date',)
   
    context = {
        'bpost': bpost,
        
    }
    return render(request, 'homepage/yazılım.html', context)

def gcategory(request):
    bpost = BlogPost.objects.all().order_by('-created_date',)
   
    context = {
        'bpost': bpost,
        
    }
    return render(request, 'homepage/genel.html', context)

def egcategory(request):
    bpost = BlogPost.objects.all().order_by('-created_date',)
   
    context = {
        'bpost': bpost,
        
    }
    return render(request, 'homepage/eglence.html', context)

def elcategory(request):
    bpost = BlogPost.objects.all().order_by('-created_date',)
   
    context = {
        'bpost': bpost,
        
    }
    return render(request, 'homepage/elektronik.html', context)