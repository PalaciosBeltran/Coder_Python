from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.ProductoCategoria)

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "foto")
    # list_display_links
    # list_filter
    # list_select_related
    # list_per_page
    # list_max_show_all
    # list_editable
    # search_fields
