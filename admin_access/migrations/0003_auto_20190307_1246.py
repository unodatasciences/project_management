# Generated by Django 2.1.7 on 2019-03-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_access', '0002_auto_20190221_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='advisor',
            new_name='budget',
        ),
        migrations.RemoveField(
            model_name='project',
            name='email',
        ),
        migrations.AddField(
            model_name='project',
            name='permission',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]