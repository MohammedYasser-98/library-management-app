from django.shortcuts import render

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
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about.html')

def reservation_index(request):
    
    return render(request, 'reservations/index.html', {'reservation': reservation})


