from django.db import models


# Model for Cabins
class Cabin(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class SeatReservation(models.Model):
    reservation_id = models.UUIDField()
    selected_cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    reserved_seat = models.CharField(max_length=100)
    fare = models.IntegerField()





