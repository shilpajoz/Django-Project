from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    widgets = {
        'category': forms.Select(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'des': forms.TextInput(attrs={'class': 'form-control'}),
    }
