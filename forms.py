from django import forms
from .models import prod

class ProdForm(forms.ModelForm):
     class Meta:
          model = prod
          fields = '__all__'
