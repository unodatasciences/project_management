# Generated by Django 2.0.5 on 2019-08-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0028_remove_project_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]