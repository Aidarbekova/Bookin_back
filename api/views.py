from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView, status

from api.models import Genre, Book, Order
from api.serializers import GenreSerializer, BookSerializer, OrderSerializer

@api_view(['GET'])
def genres(request):
    try:
        return Response(GenreSerializer(Genre.objects.all(), many=True).data, status=status.HTTP_200_OK)
    except:
        return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def genre(request, id):
    try:
        return Response(GenreSerializer(Genre.objects.get(id=id)).data, status=status.HTTP_200_OK)
    except:
        return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def books_by_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
        return Response(BookSerializer(genre.book_set.all(), many=True).data, status=status.HTTP_200_OK)
    except:
        return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BooksView(APIView):
    def get(self, request):
        try:
            return Response(BookSerializer(Book.objects.all(), many=True).data, status=status.HTTP_200_OK)
        except:
            return Response({"exception":"happenпатриаршие пруды ed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetailedView(APIView):
    def get(self, request, id):
        try:
            return Response(BookSerializer(Book.objects.get(id=id)).data, status=status.HTTP_200_OK)
        except:
            return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'GET'])
def order_book(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.data.get('book'))
        Order.objects.create(
            name = request.data.get('name'),
            status = request.data.get('status'),
            phone = request.data.get('phone'),
            address = request.data.get('address'),
            book = book
        )
        return Response({"":""}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        return Response(OrderSerializer(Order.objects.all(), many=True).data, status=status.HTTP_200_OK)

class OrderInfo(APIView):
    def get(self,request, id):
        return Response(OrderSerializer(Order.objects.get(id=id)).data, status=status.HTTP_200_OK)

    def put(self,request, id):
        order = Order.objects.get(id=id)
        order.status = request.data.get('status')
        order.save()
        return Response({"":""}, status=status.HTTP_200_OK)

    def delete(self,request,id):
        order = Order.objects.get(id=id)
        order.delete()
        return Response({"":""}, status=status.HTTP_200_OK)
