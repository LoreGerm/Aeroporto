# Generated by Django 4.0.3 on 2022-03-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_prenotazioni_codice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personale',
            name='codice',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]