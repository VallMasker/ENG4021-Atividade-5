# Generated by Django 5.0.2 on 2024-04-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquisitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalhespersonagem',
            name='nivel_recomendado',
        ),
    ]
