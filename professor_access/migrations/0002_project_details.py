# Generated by Django 2.1.7 on 2019-03-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='details',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
