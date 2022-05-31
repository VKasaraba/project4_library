from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.publisher import Publisher
from library.apps.books.serializers.publisher_serializer import PublisherSerializer
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated


@handle_library_exceptions
class PublisherListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


@handle_library_exceptions
class PublisherRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
