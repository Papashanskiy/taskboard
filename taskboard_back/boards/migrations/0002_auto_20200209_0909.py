# Generated by Django 3.0.3 on 2020-02-09 06:09

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(default=boards.models.get_default_title, max_length=256),
        ),
    ]
