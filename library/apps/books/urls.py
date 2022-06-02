from django.urls import path

from library.apps.books.views.author_view import AuthorListCreateAPIView, AuthorRetrieveUpdateAPIView
from library.apps.books.views.books import BookListCreateAPIView, BookRetrieveUpdateAPIView
from library.apps.books.views.publisher_view import PublisherListCreateAPIView, PublisherRetrieveUpdateAPIView
from library.apps.books.views.rent_record_view import RentRecordListCreateAPIView, RentRecordRetrieveUpdateAPIView


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateAPIView.as_view()),
    path('authors/', AuthorListCreateAPIView.as_view()),
    path('authors/<int:pk>/', AuthorRetrieveUpdateAPIView.as_view()),
    path('publishers/', PublisherListCreateAPIView.as_view()),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateAPIView.as_view()),
    path('rent_records/', RentRecordListCreateAPIView.as_view()),
    path('rent_records/<int:pk>/', RentRecordRetrieveUpdateAPIView.as_view()),
]
