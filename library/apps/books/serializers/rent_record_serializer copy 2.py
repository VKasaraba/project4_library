from rest_framework import serializers
from library.apps.books.models.rent_record import RentRecord


class RentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRecord
        fields = '__all__'
