# Generated by Django 5.0.2 on 2024-04-19 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquisitor', '0010_remove_classe_icone_remove_personagem_icone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personagem',
            old_name='rank',
            new_name='idade',
        ),
    ]
