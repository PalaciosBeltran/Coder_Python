from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
        path("destino_categoria_list/", views.destino_categoria_list, name="destino_categoria_list"),
        path("destino_categoria_create/", views.destino_categoria_create, name="destino_categoria_create"),
]