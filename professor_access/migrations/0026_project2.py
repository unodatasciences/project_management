# Generated by Django 2.0.6 on 2019-08-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor_access', '0025_auto_20190718_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('advisor', models.CharField(max_length=200)),
                ('stage', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
