from django.shortcuts import render, HttpResponse
from .models import Produto

# Create your views here.

def home(request):
    hamburguers = Produto.objects.all()
    return render(request, 'home.html', {'hamburguers': hamburguers})


def produto(request, burguer_id):
    item = Produto.objects.get(pk=burguer_id)
    return render(request, 'produto.html', {'item':item})