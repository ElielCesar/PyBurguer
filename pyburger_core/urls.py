
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('burguer.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Nome na página de Login e no header do django admin
admin.site.site_header = 'PyBurguer - Sistema de Hamburguerias'    
# Nome que aparece no titulo da aba do navegador
admin.site.site_title = 'PyBurguer'                                         
# Nome no lado esquerdo do painel django admin
admin.site.index_title = 'PyBurguer'                          