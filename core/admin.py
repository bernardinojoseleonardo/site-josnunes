from django.contrib import admin
from .models import Servico, Foto, Contacto

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'ordem']
    list_editable = ['ordem']
    list_filter = ['categoria']
    search_fields = ['nome', 'descricao']

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'destaque', 'visivel', 'data_upload']
    list_filter = ['categoria', 'destaque', 'visivel']
    search_fields = ['titulo']
    list_editable = ['destaque', 'visivel']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    list_filter = ['lido']
    readonly_fields = ['nome', 'email', 'mensagem', 'data']
    search_fields = ['nome', 'email', 'mensagem']
