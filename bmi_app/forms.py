#forms.py

from django import forms
from .models import BMI_model

class ImageForm(forms.ModelForm):

    class Meta:
        model = BMI_model
        fields = ['age', 'gender', 'image']
