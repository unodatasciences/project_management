# Generated by Django 2.0.6 on 2019-04-16 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0006_auto_20190416_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='advisor',
            new_name='instructor',
        ),
    ]