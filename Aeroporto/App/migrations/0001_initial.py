# Generated by Django 4.0 on 2022-03-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aereo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targa', models.CharField(max_length=50, unique=True)),
                ('modello', models.CharField(max_length=50, unique=True)),
                ('stato', models.CharField(max_length=50)),
                ('prima_classe', models.IntegerField()),
                ('seconda_classe', models.IntegerField()),
                ('terza_classe', models.IntegerField()),
                ('km_totali', models.IntegerField()),
                ('km_da_ultima_manutenzione', models.IntegerField()),
                ('data_ultima_manutenzione', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Aeroporto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.CharField(max_length=200, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('descrizione', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Turni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('ora', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Volo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.CharField(max_length=200, unique=True)),
                ('ora_p', models.TimeField()),
                ('ora_a', models.TimeField()),
                ('data_p', models.DateField()),
                ('data_a', models.DateField()),
                ('km', models.FloatField()),
                ('aereo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.aereo')),
                ('aeroporto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.aeroporto')),
            ],
        ),
        migrations.CreateModel(
            name='Personale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.CharField(max_length=50, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('stato', models.CharField(max_length=50)),
                ('ruolo', models.CharField(max_length=50)),
                ('aereo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.aereo')),
            ],
        ),
        migrations.CreateModel(
            name='Indirizzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('via', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('citta', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=2)),
                ('stato', models.CharField(max_length=100)),
                ('personale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.personale')),
            ],
        ),
        migrations.CreateModel(
            name='Has_volo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroporto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.aeroporto')),
                ('volo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.volo')),
            ],
        ),
        migrations.CreateModel(
            name='Has_turni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.personale')),
                ('turni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.turni')),
            ],
        ),
        migrations.AddField(
            model_name='aeroporto',
            name='indirizzo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.indirizzo'),
        ),
    ]
