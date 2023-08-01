from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from reservation_app.serializers import SeatReservationSerializer, CabinSerializer
from reservation_app.models import SeatReservation
from rest_framework import status
from reservation_app.utils import BaseUtilClass
from reservation_app.models import Cabin
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
log = logging.getLogger(__name__)


class CabinList(APIView):

    """
    List all the record present in cabin model
    """
    def get(self, request):
        cabin_detail = Cabin.objects.all()
        serializer = CabinSerializer(cabin_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Fetch client data and saves new  Cabin record to Database table
    """
    def post(self, request):
        cabin_request_data = request.data
        serializer = CabinSerializer(data=cabin_request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeatReservationList(APIView):

    """
    Fetch Data from Seat Reservation Model and send all data in response
    """
    def get(self, request):
        reservation_detail = SeatReservation.objects.all()
        serializer = SeatReservationSerializer(reservation_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Accepts the request data from client, verifies and create the reservation Ticket 
    """
    def post(self, request):

        try:
            # Fetching required details like cabin class and family members count from request data
            client_request_data = request.data
            log.info(f"Data Received from client end --> {client_request_data}")
            cabin_data = client_request_data['cabin']
            family_members = int(client_request_data['members'])

            # Query the database for Seat based on Cabin class
            cabin_class = Cabin.objects.get(name__iexact=cabin_data)
            log.info(f"The total seats in {cabin_class} --> {cabin_class.capacity}")
            log.info(f"The type of cabin seat --> {type(cabin_class.capacity)}")

            # returns the seats available based on number seats requested and available in a cin
            available_seats = BaseUtilClass.check_seat_availability(cabin_class.capacity, family_members)
            log.info(f"Total Available Seats are --> {available_seats}")

            if available_seats:
                selected_seats = BaseUtilClass.select_seats(cabin_data, family_members)
                reservation_data = BaseUtilClass.send_reservation_details(cabin_data, selected_seats)
                log.info(f"The reservation data to be sent --> {reservation_data}")
                return Response(data=reservation_data, status=status.HTTP_200_OK)
            else:
                failed_reservation_response = {
                    'message': "Sorry, there are not enough seats available to accommodate your family."
                }
                return Response(data=failed_reservation_response, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as ex:
            error_message = {
                "message": "The requested Cabin is not Available. Please provide correct Cabin from given option"
            }
            log.error(f"Something went wrong --->{ex}")
            return Response(data=error_message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_message = {
                "message": "Something went wrong!!!!"
            }
            log.error(f"Something went wrong --->{e}")
            return Response(data=error_message)



