from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.rent_record import RentRecord
from library.apps.books.serializers.rent_record_serializer import RentRecordSerializer


class RentRecordListCreateAPIView(ListCreateAPIView):
    serializer_class = RentRecordSerializer
    queryset = RentRecord.objects.all()


class PublisherRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RentRecordSerializer
    queryset = RentRecord.objects.all()