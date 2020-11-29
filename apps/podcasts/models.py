import uuid
from django.db import models

from .utils import upload_file


class AudioRecord(models.Model):
    title = models.CharField(
        "Название",
        max_length=255,
    )
    description = models.TextField("Описание", blank=True, null=True)
    file = models.FileField("Файл", null=True, upload_to=upload_file)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField("Название", max_length=255)


class PlaylistToAudioRecord(models.Model):
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE,
        related_name='audio_records',
    )
    audio_record = models.ForeignKey(
        AudioRecord,
        on_delete=models.CASCADE,
    )
    weight = models.PositiveSmallIntegerField(default=0)
