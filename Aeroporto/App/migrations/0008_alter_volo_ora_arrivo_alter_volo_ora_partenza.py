# Generated by Django 4.0.3 on 2022-03-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_admin_nome_alter_admin_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volo',
            name='ora_arrivo',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='volo',
            name='ora_partenza',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
