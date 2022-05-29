from rest_framework import serializers
from library.apps.books.models.publisher import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
