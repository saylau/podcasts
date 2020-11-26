import uuid
from django.db import models


class Gloss(models.Model):
    concept = models.CharField(
        "Концепт",
        max_length=255,
    )
    interpretation = models.TextField("Толкование")

    def __str__(self):
        return self.concept

    class Meta:
        verbose_name = "Глосса"
        verbose_name_plural = "Глоссарий"
