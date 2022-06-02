from rest_framework import serializers
from library.apps.books.models.rent_record import RentRecord
from library.apps.books.price_manager.price_manager import PriceManager


class RentRecordSerializer(serializers.ModelSerializer):
    rent_price = serializers.SerializerMethodField()

    class Meta:
        model = RentRecord
        fields = '__all__'

    def get_rent_price(self, obj):
        price_manager = PriceManager()
        return price_manager.calculate_rent_price(obj.book, obj.user, obj.weeks_number)
