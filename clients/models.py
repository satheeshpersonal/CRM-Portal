from django.db import models
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from siteconfig.functions import filename_conversion

# Create your models here.
STATUSCHOICES = (
    ("A", "Active"),
    ("I", "Inactive"),
    ("D", "Deleted"),
)


def document_directory_path(instance, filename):
    return 'document/{0}/{1}'.format(filename_conversion(instance.created_by.username), filename_conversion(filename))

class Document(models.Model):
    
    id = models.UUIDField(default = uuid.uuid4,primary_key = True,error_messages={
        "invalid": '(Usability_review) Is Not Valid.'
    })
    document_file = models.FileField(max_length=250, upload_to = document_directory_path, blank=True)

    status = models.CharField(max_length=1, choices=STATUSCHOICES, default="A")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='document_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='document_updated_by', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


# def project_image_directory_path(instance, filename):
#     return 'usability_review/{0}/{1}'.format(filename_conversion(instance.name), filename_conversion(filename))

class Clients(models.Model):
    
    id = models.UUIDField(default = uuid.uuid4,primary_key = True,error_messages={
        "invalid": '(Usability_review) Is Not Valid.'
    })
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, related_name='document', blank=True, null=True)
    horodateur = models.DateTimeField(null=True, blank=True)
    adresse_e_mail = models.CharField(max_length=1000, default="", null=True, blank=True)
    nom_postnom_et_prenom = models.CharField(max_length=1000, default="", null=True, blank=True)
    lieu_date_de_naissance = models.CharField(max_length=1000, default="", null=True, blank=True)
    adresse_email = models.CharField(max_length=1000, default="", null=True, blank=True)
    telephone = models.CharField(max_length=1000, default="", null=True, blank=True)
    profession = models.CharField(max_length=1000, default="", null=True, blank=True)
    etat_civil = models.CharField(max_length=1000, default="", null=True, blank=True)
    conjointe = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_benediction_nuptiale = models.DateTimeField(null=True, blank=True)
    nombre_denfants = models.CharField(max_length=1000, default="", null=True, blank=True)
    noms_prenoms_enfants = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_de_consecretion = models.CharField(max_length=1000, default="", null=True, blank=True)
    niveau_detude = models.CharField(max_length=1000, default="", null=True, blank=True)
    adresse_locale = models.CharField(max_length=1000, default="", null=True, blank=True)
    province = models.CharField(max_length=1000, default="", null=True, blank=True)
    ville = models.CharField(max_length=1000, default="", null=True, blank=True)
    pays = models.CharField(max_length=1000, default="", null=True, blank=True)
    nationalite = models.CharField(max_length=1000, default="", null=True, blank=True)
    communion = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateurcommunion = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateur_asst_communion = models.CharField(max_length=1000, default="", null=True, blank=True)
    sec_tresorier_communion = models.CharField(max_length=1000, default="", null=True, blank=True)
    adresse_communion = models.CharField(max_length=1000, default="", null=True, blank=True)
    telephone_coordonnateur_communion = models.CharField(max_length=1000, default="", null=True, blank=True)
    rameau = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateur_rameau = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateur_assist_rameau = models.CharField(max_length=1000, default="", null=True, blank=True)
    sec_tresorier_rameau = models.CharField(max_length=1000, default="", null=True, blank=True)
    secteur = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateur_secteur = models.CharField(max_length=1000, default="", null=True, blank=True)
    secretaire_secteur = models.CharField(max_length=1000, default="", null=True, blank=True)
    section = models.CharField(max_length=1000, default="", null=True, blank=True)
    coordonnateur_de_section = models.CharField(max_length=1000, default="", null=True, blank=True)
    secretaire_section = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_1er_cours_fondamental_fr = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_1er_cours_intermediaire_fr = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_1er_cours_vivre_la_parole_de_dieu_en_famille = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_fondamentale_en_anglais = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_defeating_the_adversary = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_living_the_book_of_acts = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_avance = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_renewing_the_mind = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_practical_keys = models.CharField(max_length=1000, default="", null=True, blank=True)
    date_cours_living = models.CharField(max_length=1000, default="", null=True, blank=True)
    fonction_au_ministere = models.CharField(max_length=1000, default="", null=True, blank=True)
    
    status = models.CharField(max_length=1, choices=STATUSCHOICES, default="A")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class ClientAccess(models.Model):
    
    # id = models.UUIDField(default = uuid.uuid4,primary_key = True,error_messages={
    #     "invalid": '(Usability_review) Is Not Valid.'
    # })
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='clients', blank=True, null=True)
    shared_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='shared_user', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUSCHOICES, default="A")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.id