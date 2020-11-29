from rest_framework import serializers

from .models import Gloss


class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gloss
        fields = "__all__"
