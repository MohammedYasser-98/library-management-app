from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=13, unique=True)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.id})

    

class Reservation(models.Model):
    borrow_date = models.DateField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.due_date.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse('reservation-detail', kwargs={'reservation_id': self.id})
    book = models.ManyToManyField(Book)
    user = models.ForeignKey(User, on_delete=models.CASCADE)