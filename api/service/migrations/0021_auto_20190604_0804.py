# Generated by Django 2.2 on 2019-06-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_auto_20190530_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionvideo',
            name='mime_type',
            field=models.CharField(default='video/avi', max_length=50),
        ),
    ]