# Generated by Django 4.0.2 on 2022-05-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caregiver',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
