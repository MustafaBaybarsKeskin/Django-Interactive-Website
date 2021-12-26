from django import forms
from .models import Gundem
class GundemForm(forms.ModelForm):
    class Meta:
        model = Gundem
        fields = ["title","content"]