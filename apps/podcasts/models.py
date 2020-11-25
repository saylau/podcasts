import uuid
from django.db import models

class AudioRecord(models.Model):
    title = models.UUIDField(
        "Название",
    )
    file = models.FileField("Файл")

    def __str__(self):
        return self.username
