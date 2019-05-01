from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Kontakt
 

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Taka nazwa użytkownika już istnieje')
                return redirect ('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Użytkownik z takim emailem już istnieje')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name )
                    #auth.login(request, user)
                    #messages.success(request, 'Jesteś zalogowany')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'Zostałeś zarejestrowany, teraz możesz się zalogować')
                    return redirect('login')
        else:
            messages.error(request, 'Hasła nie zgadzają się')
            return redirect('register')

        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

    # Logowanie użytkownika

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Zostałeś zalogowany")
            return redirect('dashboard')
        else:
            messages.errort(request, 'błędne hasło lub nazwa użytkownika')
            return redirect('login')

    
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'Zostałeś wylogowany')
        return redirect('index')

def dashboard(request):
    zapytania_uzytkownika = Kontakt.objects.order_by('-data_kontaktu').filter(uzytkownik_id=request.user.id)

    context = {
        'zapytania': zapytania_uzytkownika
    }

    return render(request,'accounts/dashboard.html',context)
