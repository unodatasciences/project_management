# Generated by Django 2.0.6 on 2019-04-26 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0011_auto_20190426_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='email',
        ),
    ]
