from django import forms
from django.contrib.auth.models import User
from .models import Groupe, Activite

class InscriptionSousAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['nom']

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['date', 'jour', 'tutaingiliya', 'muhubiri', 'kiongozi', 'annonces']