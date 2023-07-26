from django.db import models
from rest_framework.serializers import ModelSerializer

class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  isbn = models.CharField(max_length=255)
  published_date = models.DateTimeField()

class BookSerializer(ModelSerializer):
  model = Book
  fields = ("id","title","author","isbn","published_date")