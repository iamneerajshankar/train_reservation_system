from django.contrib import admin
from reservation_app.models import Cabin, SeatReservation
# Register your models here.


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']


@admin.register(SeatReservation)
class CabinAdmin(admin.ModelAdmin):
    list_display = ['reservation_id', 'selected_cabin', 'reserved_seat', 'fare']

