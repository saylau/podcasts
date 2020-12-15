from django.contrib import admin

from .models import TestQuestion, Test, TestQuestionAnswer, Category

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(TestQuestionAnswer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
