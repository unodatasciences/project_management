# Generated by Django 2.0.5 on 2019-08-30 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0027_project_advisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='file',
        ),
    ]