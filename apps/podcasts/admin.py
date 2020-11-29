from django.contrib import admin

from .models import AudioRecord, Playlist, PlaylistToAudioRecord


@admin.register(AudioRecord)
class AudioRecordAdmin(admin.ModelAdmin):
    pass


class PlaylistToAudioRecordInline(admin.TabularInline):
    model = PlaylistToAudioRecord


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistToAudioRecordInline]
