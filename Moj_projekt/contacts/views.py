from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Kontakt

# Create your views here.
def contact(request):
    if request.method == "POST":
        oferta_id = request.POST['oferta_id']
        oferta = request.POST['oferta']
        nazwa = request.POST['nazwa']
        email = request.POST['email']
        telefon = request.POST['telefon']
        wiadomosc = request.POST['wiadomosc']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']
        kontakt = Kontakt(oferta=oferta, oferta_id=oferta_id, nazwa=nazwa, email=email, telefon=telefon, wiadomosc=wiadomosc, uzytkownik_id = user_id )
        kontakt.save()
        
        messages.success(request, 'Twoje zapytanie zostało wysłane, nasz agent wkrótce się z Tobą skontaktuje')
        
        return redirect('/listings/'+ oferta_id)