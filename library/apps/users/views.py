from django.shortcuts import render

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from library.apps.users.models import User
from library.apps.users.serializers import UserSerializer
from library.apps.utils.custom_exception_handler import handle_library_exceptions
from rest_framework.permissions import IsAuthenticated


@handle_library_exceptions
class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()


@handle_library_exceptions
class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
