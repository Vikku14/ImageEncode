from Encode.models import ImageData
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageData
        fields= '__all__'
        extra_kwargs = { 'hash_format': {'required': False} ,
                        'base64_format': {'required': False}
         }
