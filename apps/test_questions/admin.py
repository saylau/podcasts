from django.contrib import admin

from .models import TestQuestion, Test

@admin.register(Test)
@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    pass
