from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm 
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from user import views
# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"article/exforum.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request,"article/exforum.html",{"articles":articles})

@login_required(login_url = "login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "sayfagirdisi":5,
        "articles":articles,
    }
    return render(request,"article/dashboard.html",context)

@login_required(login_url = "login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Konunuz başarıyla açılmıştır.")
        return redirect("article:articles")

    return render(request,"article/addarticle.html",{"form":form})

def exforum(request,id):
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"article/exforum.html",{"article":article,"comments":comments})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request,"article/detail.html",{"article":article,"comments":comments})

@login_required(login_url = "login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance= article)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Konunuz başarıyla güncellendi.")
        return redirect("article:articles")

    return render(request,"article/update.html",{"form":form})

@login_required(login_url = "login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()

    messages.success(request,"Konu Başarıyla Silindi")

    return redirect("article:dashboard")


def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))

#def detail(request,id):   #burası birden cok dinamik url tanımlamamıza sagliyor.
#    return HttpResponse("Detail: "+ str(id))