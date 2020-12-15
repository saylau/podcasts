import uuid
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='test/categories/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Test(models.Model):
    title = models.CharField(
        "Название",
        max_length=255
    )
    image = models.ImageField(upload_to='test/images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')

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
        verbose_name="Вопрос",
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
