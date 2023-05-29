from django import forms

from . import models


class DestinoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.DestinoCategoria
        fields = "__all__"
