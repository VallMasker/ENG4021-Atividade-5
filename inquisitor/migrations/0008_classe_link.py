# Generated by Django 5.0.2 on 2024-04-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquisitor', '0007_alter_personagem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]