from django.db import models
from django.contrib.auth.models import User

class Groupe(models.Model):
    nom = models.CharField(max_length=100)
    admin_principal = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groupes_administres')
    sous_admin = models.ManyToManyField(User, related_name='groupes', blank=True)

    def __str__(self):
        return self.nom

class Activite(models.Model):
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, related_name='activites')
    date = models.DateField()
    jour = models.CharField(max_length=50)
    tutaingiliya = models.CharField(max_length=100)
    muhubiri = models.CharField(max_length=100)
    kiongozi = models.CharField(max_length=100)
    annonces = models.TextField()

    def __str__(self):
        return f"{self.jour} - {self.groupe.nom}"