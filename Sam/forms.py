from django import forms
from .models import Item, Job


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields ="__all__"

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields ="__all__"

