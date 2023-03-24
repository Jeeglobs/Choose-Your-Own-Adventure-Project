from rest_framework import serializers
from .models import User, Book, Author, Tracker


class TrackerSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()

    class Meta:
        model = Tracker
        fields = (
            'user',
            'book',
            'status',
        )


class UserSerializer(serializers.ModelSerializer):
    tracker_instances = TrackerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'tracker_instances',
        )


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            '_published',
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
