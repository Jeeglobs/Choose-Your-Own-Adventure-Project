from rest_framework import serializers
from .models import User, Book, Author, Tracker


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'date_published',
            'genre',
            'blurb',
            'featured',
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'name',
            'dob',
            'bio',
        )


class TrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracker
        fields = (
            'user',
            'book',
            'status',
        )
