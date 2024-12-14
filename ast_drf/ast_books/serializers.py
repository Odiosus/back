from rest_framework import serializers
from .models import Review, Book, BookPicture


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'video_url', 'price_url', 'motion_object']


class BookPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPicture
        fields = ['id', 'title', 'image', 'book']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'create', 'text', 'pros']
