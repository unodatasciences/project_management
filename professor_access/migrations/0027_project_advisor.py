# Generated by Django 2.0.6 on 2019-08-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0026_project2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='advisor',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]