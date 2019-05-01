from django.contrib import admin
from .models import Kontakt
# Register your models here.

class KontaktAdmin(admin.ModelAdmin):
    list_display = ('id','nazwa', 'oferta', 'email', 'data_kontaktu')
    list_display_links = ('id', 'nazwa')
    search_fields = ('nazwa', 'email', 'oferta')
    list_per_page = 20



admin.site.register(Kontakt, KontaktAdmin)