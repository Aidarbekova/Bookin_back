from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('genres/', views.genres),
    path('books/', views.BooksView.as_view()),

    path('genres/<int:id>/books/', views.books_by_genre),
    path('order/', views.order_book),

    path('genres/<int:id>/', views.genre),
    path('books/<int:id>/', views.BookDetailedView.as_view()),
    path('order/<int:id>/', views.OrderInfo.as_view()),

    path('login/', obtain_jwt_token)
]