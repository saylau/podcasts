import uuid
from django.db import models


class Test(models.Model):
    title = models.CharField(
        "Название",
        max_length=255
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class TestQuestion(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name="Тест",
        related_name='questions'
        )
    question = models.TextField('Вопрос')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class TestQuestionAnswer(models.Model):
    test_question = models.ForeignKey(
        TestQuestion,
        verbose_name="Тест",
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answer = models.TextField("Ответ")
    is_right = models.BooleanField("Правильный", default=False)
    
    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
