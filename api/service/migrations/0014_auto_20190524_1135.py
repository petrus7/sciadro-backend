# Generated by Django 2.2 on 2019-05-24 11:35

from django.db import migrations, models
import django.db.models.deletion
import service.models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20190524_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='height',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='width',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='video_file',
        ),
        migrations.CreateModel(
            name='MissionVideo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('video_file', models.FileField(upload_to=service.models.upload_to)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission_vid', to='service.Mission')),
            ],
            options={
                'db_table': 'mission_video',
            },
        ),
    ]
