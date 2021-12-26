

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
#burada yapılan işleme göre görüntüler döndürülür

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #sırada password ve username ile eşleşen bir data database de varmı diye sorgu işlemi yapıcaz

        user = auth.authenticate(username = username, password = password)

        if user is not None:#yani none değilse
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Oturum açıldı')
            return redirect('homepage')
        else:
            messages.add_message(request, messages.ERROR, 'Yanlış kullanıcı adı veya şifre girdiniz. Lütfen tekrar deneyiniz.')
            return redirect('login')

    else:
        return render(request, 'user/login.html')




def register(request):
    if request.method == 'POST':
        #user akyıt
        #get form values

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #username kontrol daha önce alınmışmı 
            if User.objects.filter(username = username).exists(): #burada filtre işlemi yapar ve true false döndürür
                messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı daha önce alınmış')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists(): #burada filtre işlemi yapar ve true false döndürür
                    messages.add_message(request, messages.WARNING, 'Bu email daha önce alınmış')
                    return redirect('register')
                else:
                    #bütün olasılıklar kontrol edildi
                    #şimdi kayıt işlemi
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu')
                    return redirect('login')#en son login i döndür
        else:
            print('Parolalar eşleşmiyor')
            return redirect('register')

    else:
        return render(request, 'user/register.html')


    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturumunuz kapatıldı.')
        return redirect('homepage')



