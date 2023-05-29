from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("producto/", include(("producto.urls", "producto"))),
    path("usuario/", include(("usuario.urls", "usuario"))),
    path("destino/", include(("destino.urls", "destino"))),
]
