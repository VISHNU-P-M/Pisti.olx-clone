# Generated by Django 3.1.5 on 2021-04-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='fuel',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='km_driven',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
