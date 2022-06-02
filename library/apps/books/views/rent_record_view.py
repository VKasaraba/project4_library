from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.rent_record import RentRecord
from library.apps.books.serializers.rent_record_serializer import RentRecordSerializer
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated


@handle_library_exceptions
class RentRecordListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RentRecordSerializer
    queryset = RentRecord.objects.all()


@handle_library_exceptions
class RentRecordRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RentRecordSerializer
    queryset = RentRecord.objects.all()
