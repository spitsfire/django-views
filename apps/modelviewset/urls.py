from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = router.urls