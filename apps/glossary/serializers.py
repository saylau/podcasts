from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from phonenumber_field.serializerfields import PhoneNumberField

from apps.people.models import PersonalData


class ClientDeliveryDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDeliveryDocument
        fields = "__all__"