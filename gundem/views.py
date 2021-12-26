from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import GundemForm 
from django.contrib import messages
from .models import Gundem,Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

def gundemler(request):
    keyword = request.GET.get("keyword")
    if keyword:
        gundemler = Gundem.objects.filter(title__contains = keyword)
        return render(request,"gundem/gundemler.html",{"gundemler":gundemler})
    gundemler = Gundem.objects.all()
    return render(request,"gundem/gundemler.html",{"gundemler":gundemler})




def index(request):
    context = {
        "sayfagirdisi":5
    }
    return render(request,"gundem/index.html",context)

@login_required(login_url = "login")
def dashboard(request):
    gundemler = gundem.objects.filter(author = request.user)
    context = {
        "sayfagirdisi":5,
        "gundemler":gundemler,
    }
    return render(request,"gundem/dashboard.html",context)

@login_required(login_url = "login")
def gundemEkle(request):
    form = GundemForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        gundem = form.save(commit=False)
        gundem.author = request.user
        gundem.save()
        messages.success(request,"Gündem yazınız başarıyla oluşturulmuştur.")
        return redirect("gundem:gundemler")

    return render(request,"gundem/gundemekle.html",{"form":form})

def exforum(request,id):
    gundem = get_object_or_404(gundem,id=id)
    comments = gundem.comments.all()
    return render(request,"gundem/exforum.html",{"gundem":gundem,"comments":comments})
    
@xframe_options_exempt
def detail(request,id):
    #gundem = gundem.objects.filter(id = id).first()
    gundem = get_object_or_404(Gundem,id = id)
    comments = gundem.comments.all()
    return render(request,"gundem/detail.html",{"gundem":gundem,"comments":comments})

@login_required(login_url = "login")
def gundemGuncelle(request,id):
    gundem = get_object_or_404(gundem,id = id)
    form = GundemForm(request.POST or None,request.FILES or None,instance= gundem)
    
    if form.is_valid():
        gundem = form.save(commit=False)
        gundem.author = request.user
        gundem.save()
        messages.success(request,"Yazı başarıyla güncellendi.")
        return redirect("forum")

    return render(request,"gundem/update.html",{"form":form})

@login_required(login_url = "login")
def gundemSil(request,id):
    gundem = get_object_or_404(gundem,id = id)
    gundem.delete()

    messages.success(request,"Konu Başarıyla Silindi")

    return redirect("gundem:dashboard")


def addComment(request,id):
    gundem = get_object_or_404(Gundem,id = id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.gundem = gundem

        newComment.save()
    return redirect(reverse("gundem:detail",kwargs={"id":id}))

#def detail(request,id):   #burası birden cok dinamik url tanımlamamıza sagliyor.
#    return HttpResponse("Detail: "+ str(id))