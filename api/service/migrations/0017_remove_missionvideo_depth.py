# Generated by Django 2.2 on 2019-05-28 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20190528_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missionvideo',
            name='depth',
        ),
    ]
