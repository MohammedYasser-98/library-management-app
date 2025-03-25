from django.db import models
from datetime import date

class Reservation(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return self.due_date.strftime("%Y-%m-%d")