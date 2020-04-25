from django.urls import path
from api import views

urlpatterns = [
    path('genres/', views.genres),
    path('books/', views.BooksView.as_view()),

    path('genres/<int:id>/books/', views.books_by_genre),

    path('genres/<int:id>/', views.genre),
    path('books/<int:id>/', views.BookDetailedView.as_view()),

]