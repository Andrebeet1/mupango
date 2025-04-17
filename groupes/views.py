from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Groupe, Activite
from .forms import InscriptionSousAdminForm, GroupeForm, ActiviteForm

def inscription_sous_admin(request):
    if request.method == 'POST':
        form = InscriptionSousAdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('connexion')
    else:
        form = InscriptionSousAdminForm()
    return render(request, 'groupes/inscription.html', {'form': form})

def creer_groupe(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            groupe = form.save(commit=False)
            groupe.admin_principal = request.user
            groupe.save()
            return redirect('liste_groupes')
    else:
        form = GroupeForm()
    return render(request, 'groupes/creer_groupe.html', {'form': form})

def liste_activites(request, groupe_id):
    groupe = Groupe.objects.get(id=groupe_id)
    activites = groupe.activites.all()
    return render(request, 'groupes/liste_activites.html', {'groupe': groupe, 'activites': activites})