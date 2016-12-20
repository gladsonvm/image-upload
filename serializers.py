from rest_framework import serializers
from .models import FileUploads


class FileUploadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        user_id = self.context.get('request').user.id
        validated_data.update({'uploaded_by_id': user_id})
        return FileUploads.objects.create(**validated_data)

    def validate_file(self, value):
        if value.content_type.split('/')[0] == 'image' and value.size < 25000000:
            return value
        raise serializers.ValidationError('Error: Upload an image with file size below 25Mb.')

    class Meta:
        model = FileUploads
        fields = ('filename', 'image')
        lookup_field = 'filename'
        extra_kwargs = {
            'url': {'lookup_field': 'filename'}
        }
