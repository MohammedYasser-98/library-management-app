from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservation_index, name='reservation-index'),
    path('reservations/<int:reservation_id>/', views.reservation_detail, name='reservation-detail'),
]