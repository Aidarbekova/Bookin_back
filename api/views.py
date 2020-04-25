from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView, status

from api.models import Genre, Book
from api.serializers import GenreSerializer, BookSerializer

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
            return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetailedView(APIView):
    def get(self, request, id):
        try:
            return Response(BookSerializer(Book.objects.get(id=id)).data, status=status.HTTP_200_OK)
        except:
            return Response({"exception":"happened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


