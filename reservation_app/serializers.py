from rest_framework import serializers
from reservation_app.models import Cabin, SeatReservation


class CabinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin
        fields = ['name', 'capacity']


class SeatReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatReservation
        fields = '__all__'
