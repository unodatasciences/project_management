# Generated by Django 2.0.6 on 2019-04-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0013_auto_20190426_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload'),
        ),
    ]
