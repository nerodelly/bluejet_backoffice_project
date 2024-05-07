from django import forms
from .models import File

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'etat', 'taille']

class PredictionForm(forms.Form):
    measure_sensor_choices = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        # Ajoutez d'autres choix au besoin
    ]
    champs_a_predire = forms.ChoiceField(choices=measure_sensor_choices, label="Champs à prédire")
    
    farmer_choices = [
        ('farm1', 'Farm 1'),
        ('farm2', 'Farm 2'),
        # Ajoutez d'autres choix au besoin
    ]
    choisir_nom_fermier = forms.ChoiceField(choices=farmer_choices, label="Choisir le nom du fermier")
    
    prediction_date = forms.DateField(label="Date de prédiction", widget=forms.DateInput(attrs={'type': 'date'}))
