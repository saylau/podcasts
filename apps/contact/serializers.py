from rest_framework import serializers
from .models import City, Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class ContactCitySerializer(serializers.ModelSerializer):

    contacts = ContactSerializer(many=True)

    class Meta:
        model = City
        fields = '__all__'