# Generated by Django 2.2 on 2019-05-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_auto_20190527_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionvideo',
            name='fps',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='missionvideo',
            name='mime_type',
            field=models.CharField(default='video/mp4', max_length=50),
        ),
    ]