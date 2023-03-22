from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import User, Book, Author, Tracker
from .serializers import UserSerializer, BookSerializer, AuthorSerializer, TrackerSerializer


# need to make it so that ONLY admins can set as 'featured' when creating
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['featured']
    search_fields = ['title', 'author__name']


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


# need to make it so user can only view/create for themselves NOT other users
class TrackerListCreate(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


# need to make it so user can only view/edit/delete THEIR trackers, NOT others
class TrackerEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
