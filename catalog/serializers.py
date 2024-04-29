from rest_framework import serializers
from .models import Book, Author, Review, BookImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'message', 'date']

    def create(self, validated_data):
        book_id = self.context['book_pk']
        return Review.objects.create(book_id=book_id, **validated_data)


class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ['id', 'image']

    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookImage.objects.create(book_id=book_id, **validated_data)
