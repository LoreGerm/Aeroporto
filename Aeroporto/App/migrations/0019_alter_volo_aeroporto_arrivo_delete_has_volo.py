# Generated by Django 4.0 on 2022-03-28 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_volo_aeroporto_arrivo_alter_volo_aeroporto_partenza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volo',
            name='aeroporto_arrivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aeroporto_arrivo', to='App.aeroporto'),
        ),
        migrations.DeleteModel(
            name='Has_volo',
        ),
    ]
