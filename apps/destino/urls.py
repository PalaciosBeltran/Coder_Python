from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
        path("destino_categoria_list/", views.destino_categoria_list, name="destino_categoria_list"),
        path("destino_categoria_create/", views.destino_categoria_create, name="destino_categoria_create"),
    #     path("producto_categoria_delete/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
    #     path("producto_categoria_update/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
    # path("productocategoria/detail/<int:pk>", views.producto_categoria_detail, name="productocategoria_detail"),
]

urlpatterns += [
    # path("", views.IndexView.as_view(), name="index"),
    # path("destinocategoria/list/", views.DestinoCategoriaList.as_view(), name="destinocategoria_list"),
    # path("destinocategoria/create/", views.DestinoCategoriaCreate.as_view(), name="destinocategoria_create"),
    # path("productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
    # path("productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    # path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
]