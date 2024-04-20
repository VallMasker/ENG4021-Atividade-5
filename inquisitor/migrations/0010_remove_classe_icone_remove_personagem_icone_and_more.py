# Generated by Django 5.0.2 on 2024-04-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquisitor', '0009_alter_personagem_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='icone',
        ),
        migrations.RemoveField(
            model_name='personagem',
            name='icone',
        ),
        migrations.AddField(
            model_name='classe',
            name='icone_URL',
            field=models.URLField(default='https://example.com/default-icon.jpg', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personagem',
            name='icone_URL',
            field=models.URLField(default='https://example.com/default-icon.jpg', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classe',
            name='link',
            field=models.URLField(),
        ),
    ]
