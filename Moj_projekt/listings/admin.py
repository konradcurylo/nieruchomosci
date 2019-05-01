from django.contrib import admin
from .models import Oferty
# Register your models here.


class OfertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'tytul','czy_opublikowane', 'cena', 'data_oferty', 'agent')
    list_display_links = ('id','tytul')
    list_filter = ('agent','tytul',)
    list_editable = ('czy_opublikowane',)
    search_fields = ('tytul', 'opis', 'miasto', 'wojewodztwo', 'cena')
    list_per_page = 25

admin.site.register(Oferty, OfertyAdmin)
