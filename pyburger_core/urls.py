
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('burguer.urls'))
]



# Nome na página de Login e no header do django admin
admin.site.site_header = 'PyBurguer - Sistema de Hamburguerias'    
# Nome que aparece no titulo da aba do navegador
admin.site.site_title = 'PyBurguer'                                         
# Nome no lado esquerdo do painel django admin
admin.site.index_title = 'PyBurguer'                          