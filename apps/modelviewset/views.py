from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework import status
from main.models import Book, BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer