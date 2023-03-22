from django.shortcuts import render
from rest_framework import generics

from .models import User, Book, Author, Tracker
from .serializers import UserSerializer, BookSerializer, AuthorSerializer, TrackerSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
