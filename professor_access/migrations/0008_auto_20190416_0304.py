# Generated by Django 2.0.6 on 2019-04-16 03:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0007_auto_20190416_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
