from django.contrib import admin
from galery.models import *

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id","nome")
    search_fields = ("nome",)

admin.site.register(Fotografia, ListandoFotografias)
