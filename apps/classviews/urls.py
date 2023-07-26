from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:id>/', views.BookDetail.as_view()),
]
