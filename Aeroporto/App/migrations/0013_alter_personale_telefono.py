# Generated by Django 4.0 on 2022-03-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_volo_aeroporto_arrivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personale',
            name='telefono',
            field=models.CharField(max_length=100, null=True),
        ),
    ]