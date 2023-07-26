from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from main.models import Book, BookSerializer

def book_list(request):
  if request.method == "GET":
    # pasted directly from REST Framework > Serializers documentation
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)
  
  if request.method == "POST":
    # pasted directly from REST Framework > Serializers documentation
    data = JSONParser().parse(request)
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def book_detail(request,id):
  if request.method == "PUT":
    pass

  # so on and so forth

def authenticate(request):
  if request.method == "POST":
    pass