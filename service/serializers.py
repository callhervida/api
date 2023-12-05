from rest_framework import serializers
from .models import Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        extra_kwargs = {
            'uploading_file': {'required': False},
            'storing_link': {'required': False},
        }

    def validate(self, data):
        if not data.get('uploading_file') and not data.get('storing_link'):
            raise serializers.ValidationError("Either 'uploading_file' or 'storing_link' is required.")
        return data