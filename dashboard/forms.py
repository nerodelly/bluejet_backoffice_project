from django import forms
from .models import File

class UploadFileForm(forms.ModelForm):
    file = forms.FileField()