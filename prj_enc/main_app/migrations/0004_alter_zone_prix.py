# Generated by Django 3.2.4 on 2022-05-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220521_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='prix',
            field=models.IntegerField(),
        ),
    ]
