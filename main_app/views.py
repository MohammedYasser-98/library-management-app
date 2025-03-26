from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reservation, Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

# def home(request):
    
#     return render(request, 'home/home.html')

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    
    return render(request, 'about.html')

def reservation_index(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/index.html', {'reservations': reservations})

def reservation_detail(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    books_reservation_doesnt_have = Book.objects.exclude(id__in = reservation.book.all().values_list('id'))
    return render(request, 'reservations/detail.html', {'reservation': reservation, 'books': books_reservation_doesnt_have},)


class reservationCreate(CreateView):
    model = Reservation
    fields = ['borrow_date', 'due_date']

class ReservationUpdate(UpdateView):
    model = Reservation
   
    fields = ['due_date']

class ReservationDelete(DeleteView):
    model = Reservation
    success_url = '/reservations/'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def associate_book(request, reservation_id, book_id):
    
    Reservation.objects.get(id=reservation_id).book.add(book_id)
    return redirect('reservation-detail', reservation_id=reservation_id)

def remove_book(request, reservation_id, book_id):

    Reservation.objects.get(id=reservation_id).book.remove(book_id)

    return redirect('reservation-detail', reservation_id=reservation_id)