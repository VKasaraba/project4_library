from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.books.models.publisher import Publisher
from library.apps.books.serializers.publisher_serializer import PublisherSerializer


class PublisherListCreateAPIView(ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class PublisherRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()