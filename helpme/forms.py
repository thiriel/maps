from django import forms
from helpme.models import Point

from django.forms import ModelForm, Textarea

class CreatePoint(forms.ModelForm):
    class Meta:
        model = Point
        exclude = ['state']
