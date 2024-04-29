import random
import string
from .models import *

def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

for _ in range(20):
    accession = Accession.objects.create(
        code_accession=random_string(),
        nom_accession=random_string(),
        type_accession=random_string(),
        classification=random_string(),
        anciennete=random.randint(1, 100),
    )
    
    classe_herberium = ClasseHerberium.objects.create(
        code_classe_herberium=random_string(),
        numero_etagere=random.randint(1, 50),
    )

    origine = Origine.objects.create(
        numero_collection=random_string(),
        adresse_origine=random_string(),
        nom_collecteur=random_string(),
    )

    cultivars = Cultivars.objects.create(
        nom_cultivars=random_string(),
        traduction=random_string(),
        synonyme=random_string(),
    )

    observation = Observation.objects.create(
        code_caracteristique=random_string(),
        # photo should be a FileField; left empty here
        taille=random.randint(1, 200),
    )

    caracteristiques_fruits = CaracteristiquesFruits.objects.create(
        code_caracteristique_fruits=random_string(),
        forme_de_fruit=random_string(),
        couleur_peau=random_string(),
        couleur_chair=random_string(),
        poids=random.uniform(1.0, 10.0),
        teneur_de_sucre=random.uniform(0.0, 1.0),
    )

    SemenceGroup.objects.create(
        accession=accession,
        classe_herberium=classe_herberium,
        origine=origine,
        cultivars=cultivars,
        observation=observation,
        caracteristiques_fruits=caracteristiques_fruits,
    )

print("20 Semences have been created!")
