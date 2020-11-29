from django.contrib import admin

from .models import TestQuestion


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    pass
