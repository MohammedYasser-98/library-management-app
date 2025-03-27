from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservation_index, name='reservation-index'),
    path('reservations/<int:reservation_id>/', views.reservation_detail, name='reservation-detail'),
    path('reservations/create/', views.reservationCreate.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/update/', views.ReservationUpdate.as_view(), name='reservation-update'),
    path('reservations/<int:pk>/delete/', views.ReservationDelete.as_view(), name='reservation-delete'),

    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('books/', views.BookList.as_view(), name='book-index'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

    
    path('reservations/<int:reservation_id>/associate-book/<int:book_id>/', views.associate_book, name='associate-book'),
    path('reservations/<int:reservation_id>/remove-book/<int:book_id>/', views.remove_book, name='remove-book'),

    path('accounts/signup/', views.signup, name='signup'),
]