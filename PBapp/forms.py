from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields='__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields='__all__'

