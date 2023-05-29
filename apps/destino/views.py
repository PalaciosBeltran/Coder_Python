from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms, models

def index(request: HttpRequest) -> HttpResponse:
    categorias = models.DestinoCategoria.objects.all()[:4]
    context = {"categorias": categorias}
    return render(request, "destino/index.html", context)

def destino_categoria_list(request):
    categorias = models.DestinoCategoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "destino/destino_categoria_list.html", context)

def destino_categoria_create(request):
    if request.method == "POST":
        form = forms.DestinoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("destino:index")
    else:
        form = forms.DestinoCategoriaForm()
    return render(request, "destino/destino_categoria_create.html", {"form": form})