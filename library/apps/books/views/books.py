from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.book import Book
from library.apps.books.serializers.book_serializer import BookSerializer
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated


@handle_library_exceptions
class BookListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookSerializer
    queryset = Book.objects.all()


@handle_library_exceptions
class BookRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookSerializer
    queryset = Book.objects.all()
