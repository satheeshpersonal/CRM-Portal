# Generated by Django 4.2.13 on 2024-06-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_clients_adresse_email_alter_clients_horodateur_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='conjoint',
            new_name='adresse_e_mail',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='coordonnateur_communion',
            new_name='conjointe',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='fonction_au_ministera',
            new_name='coordonnateurcommunion',
        ),
        migrations.AddField(
            model_name='clients',
            name='fonction_au_ministere',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='date_benediction_nuptiale',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='horodateur',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]