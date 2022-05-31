from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.author import Author
from library.apps.books.serializers.author_serializer import AuthorSerializer
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated


@handle_library_exceptions
class AuthorListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


@handle_library_exceptions
class AuthorRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
