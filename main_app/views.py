from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reservation, Book
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    
    return render(request, 'about.html')

@login_required
def reservation_index(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/index.html', {'reservations': reservations})

@login_required
def reservation_detail(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    books_reservation_doesnt_have = Book.objects.exclude(id__in = reservation.book.all().values_list('id'))
    return render(request, 'reservations/detail.html', {'reservation': reservation, 'books': books_reservation_doesnt_have},)


class reservationCreate(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = ['borrow_date', 'due_date']

    def form_valid(self, form):
        
        form.instance.user = self.request.user  
        
        return super().form_valid(form)

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


def signup(request):
    error_message = ''
    if request.method == 'POST':
            
        form = UserCreationForm(request.POST)
        if form.is_valid():
                
            user = form.save()
                
            login(request, user)
            return redirect('reservation-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   