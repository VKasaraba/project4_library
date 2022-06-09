from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.book import Book
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
        user = request.user
        user_id = user.id
        data = {**self.request.data, 'user': user_id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        price_manager = PriceManager()
        book = Book.objects.get(id=data.get('book'))
        self.perform_create(serializer)
        if not self.request.data.get('opened'):
            RentRecord.objects.filter(id=serializer.data.get('id')).delete()
        else:
            book.reduce_number_of_copies(1)
            book.save()
            price_manager.pay_collateral_price(book, user)
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
        price_manager = PriceManager()
        fine = 0
        if record.is_late():
            fine = price_manager.calculate_fine(record)
            if not paid_fine:
                raise_library_exception(200, fine, 'fine')
        if record.user.balance + record.book.get_collateral_price() < price_manager.calculate_rent_price(record.book, record.user, record.weeks_number):
            raise_library_exception(400, 'Not enought money on balance')
        price_manager.return_collateral_price(record.book, record.user)
        price_manager.pay_rent_price(record.book, record.user, record.weeks_number)
        if record.is_late():
            price_manager.pay_fine(record.user, fine)
            record.user.save()
        record.closed = True
        record.book.increase_number_of_copies(1)
        record.save()
        return Response({}, status=status.HTTP_200_OK)
