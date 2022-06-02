from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.rent_record import RentRecord
from library.apps.books.price_manager.price_manager import PriceManager
from library.apps.books.serializers.rent_record_serializer import RentRecordSerializer
from library.apps.users.models import User
from library.apps.utils.custom_exception import raise_library_exception
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@handle_library_exceptions
class RentRecordListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RentRecordSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        only_active = self.request.query_params.get('only_active')
        queryset = RentRecord.objects.all()
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        if only_active:
            queryset = queryset.filter(opened=True, closed=False)
        return queryset

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        data = {**self.request.data, 'user': user_id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if not self.request.data.get('opened'):
            RentRecord.objects.filter(id=serializer.data.get('id')).delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@handle_library_exceptions
class RentRecordRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RentRecordSerializer
    queryset = RentRecord.objects.all()

    def destroy(self, request, *args, **kwargs):
        paid_fine = self.request.query_params.get('paid_fine')
        id = kwargs.get('pk')
        record = RentRecord.objects.get(id=id)
        if record.is_late() and not paid_fine:
            price_manager = PriceManager()
            fine = price_manager.calculate_fine(record)
            raise_library_exception(400, fine, 'fine')
        record.closed = True
        record.save()
        return Response({}, status=status.HTTP_200_OK)
