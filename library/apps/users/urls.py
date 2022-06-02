from django.urls import path
from library.apps.users.views import UserListCreateAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),
]
