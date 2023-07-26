from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from main.models import Book, BookSerializer

# Create your views here.
class BookList(APIView):
  def get(self,request):
    # pasted directly from REST Framework > Serializers documentation
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

  def post(self,request):
    # pasted directly from REST Framework > Serializers documentation
    data = JSONParser().parse(request)
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

class BookDetail(APIView):
  def get(self,request,id):
    pass
  def put(self,request,id):
    pass
  def delete(self,request,id):
    pass