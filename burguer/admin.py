from django.contrib import admin
from .models import *

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco']
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Produto, ProdutoAdmin)