# Generated by Django 2.0.6 on 2019-04-16 04:36

from django.db import migrations, models
import professor_access.models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0008_auto_20190416_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=professor_access.models.current_date),
        ),
    ]