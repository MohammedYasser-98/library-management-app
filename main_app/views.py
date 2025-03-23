from django.shortcuts import render
from django.http import HttpResponse

class Reservation:
    def __init__(self, borrow_date, due_date):
        self.borrow_date = borrow_date
        self.due_date = due_date
        

reservation = [
    Reservation('Jan', 'Mar'),
    Reservation('Feb', 'April'),
    Reservation('DEC', 'Mar'),
    Reservation('Nov', 'Dec'),
]



def home(request):
    
    return HttpResponse('<h1>Welcome!</h1>')

def about(request):
    
    return render(request, 'about.html')

def reservation_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'reservations/index.html')