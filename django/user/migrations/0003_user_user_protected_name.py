# Generated by Django 4.0.2 on 2022-06-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_caregiver_user_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_protected_name',
            field=models.CharField(max_length=16, null=True, verbose_name='보호대상 이름'),
        ),
    ]