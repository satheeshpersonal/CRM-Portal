# Generated by Django 4.2.13 on 2024-06-21 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewProject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, error_messages={'invalid': '(Usability_review) Is Not Valid.'}, primary_key=True, serialize=False)),
                ('horodateur', models.CharField(default='Untitled Review', max_length=500)),
                ('adresse_email', models.BooleanField(default=True)),
                ('nom_postnom_et_prenom', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='A', max_length=1)),
                ('lieu_date_de_naissance', models.IntegerField(default=1)),
                ('telephone', models.BooleanField(default=False)),
                ('etat_civil', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('conjoint', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_benediction_nuptiale', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('nombre_denfants', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('noms_prenoms_enfants', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_de_consecretion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('niveau_detude', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('adresse_locale', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('province', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('ville', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('pays', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('nationalite', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_asst_communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('sec_tresorier_communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('adresse_communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('telephone_coordonnateur_communion', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('rameau', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_rameau', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_assist_rameau', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('sec_tresorier_rameau', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('secteur', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_secteur', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('secretaire_secteur', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('section', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('coordonnateur_de_section', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('secretaire_section', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_1er_cours_fondamental_fr', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_1er_cours_intermediaire_fr', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_1er_cours_vivre_la_parole_de_dieu_en_famille', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_fondamentale_en_anglais', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_defeating_the_adversary', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_living_the_book_of_acts', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_avance', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_renewing_the_mind', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_practical_keys', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('date_cours_living', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('fonction_au_ministera', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='', max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.reviewproject')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]