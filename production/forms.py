from django import forms
from .models import Type, Category

class ProductFilterForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, empty_label="Типы",
                                    widget=forms.Select(attrs={
                                        'class': 'btn form-select'
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="Категория",
                                    widget=forms.Select(attrs={
                                        'class': 'btn form-select'
    }))