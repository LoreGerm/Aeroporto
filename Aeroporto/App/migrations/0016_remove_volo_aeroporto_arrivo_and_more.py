# Generated by Django 4.0 on 2022-03-28 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_volo_aeroporto_arrivo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volo',
            name='aeroporto_arrivo',
        ),
        migrations.AlterField(
            model_name='volo',
            name='aeroporto_partenza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aeroporto_partenza', to='App.aeroporto'),
        ),
    ]