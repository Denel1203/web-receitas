# Generated by Django 4.1.5 on 2023-01-07 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='Date_Receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
