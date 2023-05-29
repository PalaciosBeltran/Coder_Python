from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# Create your views here.
# def index(request):
#     return render(request, "destino/index.html")

# class IndexView(TemplateView):
#     template_name = "destino/index.html"

# class DestinoCategoriaList(ListView):
#     model = models.DestinoCategoria

#     def get_queryset(self):
#         # if self.request.GET.get("consulta"):
#         #     query = self.request.GET.get("consulta")
#         #     object_list = models.DestinoCategoria.objects.filter(nombre__icontains=query)
#         # else:
#         #     object_list = models.DestinoCategoria.objects.all()
#         object_list = models.DestinoCategoria.objects.all()
#         return object_list 

# class DestinoCategoriaCreate(CreateView):
#     model = models.DestinoCategoria
#     form_class = forms.DestinoCategoriaForm
#     success_url = reverse_lazy("destino:index")

# class DestinoCategoriaDetail(DetailView):
#     model = models.DestinoCategoria

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