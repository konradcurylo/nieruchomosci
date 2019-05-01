from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import cena_wybor, sypialnie_wybor, wojewodztwo_wybor
from listings.models import Oferty
from realtors.models import Agenci



# Create your views here.
def index(request):
    oferty = Oferty.objects.order_by('-data_oferty').filter(czy_opublikowane=True)[:3]

    context = {
         'oferty': oferty,
         'wojewodztwo_wybor': wojewodztwo_wybor,
         'sypialnie_wybor': sypialnie_wybor,
         'cena_wybor': cena_wybor
    }

    return render(request,'strony/index.html', context)


def about(request):
    agenci = Agenci.objects.order_by('-data_zatrudnienia')
    sprzedawca_miesiaca = Agenci.objects.all().filter(czy_sprzedawcam=True)
    context = {
        'agenci': agenci,
        'sprzedawca_miesiaca': sprzedawca_miesiaca,
    }

    return render(request,'strony/about.html',context)
