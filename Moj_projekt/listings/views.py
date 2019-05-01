from django.shortcuts import render, get_object_or_404
from .models import Oferty
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import cena_wybor, sypialnie_wybor, wojewodztwo_wybor
from realtors.models import Agenci
# Create your views here.
def index(request):

    lista_ofert = Oferty.objects.order_by('-data_oferty').filter(czy_opublikowane=True)
    paginator = Paginator(lista_ofert, 3)
    page = request.GET.get('page')
    oferty = paginator.get_page(page)
    context = {
       'oferty': oferty,
      }
    template = 'listings/listings.html'

    return render(request, template, context)


def listing(request, oferty_id):
    oferty = get_object_or_404(Oferty, pk=oferty_id)
    context = {
      'oferty':oferty
    }

    return render(request,'listings/listing.html', context)


def search(request):
    queryset_list = Oferty.objects.order_by('-data_oferty')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(opis__icontains=keywords)
   #miasto
    if 'miasto' in request.GET:
        miasto = request.GET['miasto']
        if miasto:
            queryset_list = queryset_list.filter(miasto__iexact=miasto)

    #wojewodztwo
    if 'wojewodztwo' in request.GET:
        wojewodztwo = request.GET['wojewodztwo']
        if wojewodztwo:
            queryset_list = queryset_list.filter(wojewodztwo__iexact=wojewodztwo)

       #sypialnie
    if 'sypialnie' in request.GET:
        sypialnie = request.GET['sypialnie']
        if sypialnie:
            queryset_list = queryset_list.filter(sypialnie__iexact=sypialnie)

     #cena
    if 'cena' in request.GET:
        cena = request.GET['cena']
        if cena:
            queryset_list = queryset_list.filter(cena__lte=cena)



    context = {
       'wojewodztwo_wybor': wojewodztwo_wybor,
       'sypialnie_wybor': sypialnie_wybor,
       'cena_wybor': cena_wybor,
       'oferty': queryset_list,
       'values': request.GET
    }

    return render(request, 'listings/search.html', context)
