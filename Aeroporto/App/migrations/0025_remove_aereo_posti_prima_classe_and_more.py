# Generated by Django 4.0 on 2022-03-29 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_indirizzo_a_rename_indirizzo_indirizzo_p_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aereo',
            name='posti_prima_classe',
        ),
        migrations.RemoveField(
            model_name='aereo',
            name='posti_seconda_classe',
        ),
        migrations.RemoveField(
            model_name='aereo',
            name='posti_terza_classe',
        ),
        migrations.CreateModel(
            name='Posti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posti_prima_classe', models.IntegerField(null=True)),
                ('posti_seconda_classe', models.IntegerField(null=True)),
                ('posti_terza_classe', models.IntegerField(null=True)),
                ('aereo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.aereo')),
            ],
        ),
    ]
