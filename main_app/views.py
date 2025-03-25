from django.shortcuts import render
from .models import Reservation

# class Reservation:
#     def __init__(self, borrow_date, due_date):
#         self.borrow_date = borrow_date
#         self.due_date = due_date
        

# reservation = [
#     Reservation('Jan', 'Mar'),
#     Reservation('Feb', 'April'),
#     Reservation('DEC', 'Mar'),
#     Reservation('Nov', 'Dec'),
# ]



def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about.html')

def reservation_index(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/index.html', {'reservations': reservations})

def reservation_detail(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    return render(request, 'reservations/detail.html', {'reservation': reservation})
