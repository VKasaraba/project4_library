from rest_framework import serializers
from library.apps.books.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'