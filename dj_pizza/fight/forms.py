from .models import *
from django import forms


class WarriorsSelectForm(forms.ModelForm):
    class Meta:
        model = Fight
        fields = ['description']
        labels = {'description': 'тип воина'}


class FightForm(forms.ModelForm):

    class Meta:
        model = Fight
        fields = ['kick', 'block']
        labels = {'kick': 'удар', 'block': 'блок'}
