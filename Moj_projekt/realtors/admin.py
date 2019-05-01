from django.contrib import admin
from .models import Agenci
# Register your models here.
class AgenciAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazwa', 'email', 'data_zatrudnienia')
    list_display_links = ('id', 'nazwa')
    search_fields = ('nazwa',)
    list_per_page = 25
    


admin.site.register(Agenci, AgenciAdmin)
