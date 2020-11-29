from django.contrib import admin

from .models import Gloss


@admin.register(Gloss)
class GlossAdmin(admin.ModelAdmin):
    pass
