from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<int:burguer_id>', views.produto, name='produto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 





