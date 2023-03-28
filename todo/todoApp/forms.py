from django import forms
from django.db import models
from .models import todo
# Create your models here.
class todoForm(forms.ModelForm):
    class Meta:
        model=todo
        fields='__all__'
        exclude=['date',]
        

