# Generated by Django 3.1.3 on 2020-11-29 06:37

import apps.podcasts.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('file', models.FileField(null=True, upload_to=apps.podcasts.utils.upload_file, verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistToAudioRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('audio_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcasts.audiorecord')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_records', to='podcasts.playlist')),
            ],
        ),
    ]
