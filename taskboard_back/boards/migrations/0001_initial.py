# Generated by Django 3.0.3 on 2020-02-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Task created 08-02-2020', max_length=256)),
                ('body', models.TextField()),
            ],
        ),
    ]
