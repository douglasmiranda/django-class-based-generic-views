from django.contrib import admin
from models import Audio, ListaDeReproducao


class AudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
admin.site.register(Audio, AudioAdmin)


class ListaDeReproducaoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
admin.site.register(ListaDeReproducao, ListaDeReproducaoAdmin)
