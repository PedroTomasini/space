from django.shortcuts import render, get_object_or_404
from galery.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galery/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galery/imagem.html', {"fotografia": fotografia})
