from rest_framework import serializers

from .models import AudioRecord, Playlist, PlaylistToAudioRecord


class AudioRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioRecord
        fields = "__all__"


class AudioRecordRelationSerializer(serializers.ModelSerializer):
    audio_record = AudioRecordSerializer()
    class Meta:
        model = PlaylistToAudioRecord
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    audio_records = AudioRecordRelationSerializer(many=True)
    class Meta:
        model = Playlist
        fields = "__all__"
