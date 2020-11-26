import uuid
from django.db import models


class Question(models.Model):
    question = models.TextField(
        "Вопрос"
    )
    answer = models.TextField("Ответ", null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
