from django.urls import reverse
import pytest
from rest_framework import status
from reservation_app.models import SeatReservation


class TestSeatReservationSystem:

    # Tests that the post method returns the reservation details when a reservation is successfully made
    @pytest.mark.django_db
    def test_post_method_cabin_api(self, client):
        # Make a request to save cabin record
        data = {"name": "First Class", "capacity": 5}
        response = client.post(reverse('cabin-entry'), data, content_type="application/json")

        # Check that the response status code is 201 CREATED
        assert response.status_code == status.HTTP_201_CREATED

        # Check that the response data contains the expected reservation details
        expected_data = {
            'name': 'First Class',
            'capacity': 5,
        }
        assert response.data == expected_data

    # Tests that the get method of SeatReservationList
    @pytest.mark.django_db
    def test_get_method_returns_all_seat_reservations(self, client):
        get_response = client.get(reverse('home-page'))
        # Create some SeatReservation objects
        # Call the get method of SeatReservationList
        assert get_response.status_code == 200  # URL is reachable
        assert not SeatReservation.objects.count()  # No person object exists (checking in DB)

    # Tests that the post method returns the reservation details when a reservation is successfully made
    @pytest.mark.django_db
    def test_successful_reservation(self, client):
        # Make a request to save cabin record
        data = {"name": "First Class", "capacity": 10}
        response = client.post(reverse('cabin-entry'), data, content_type="application/json")
        # Check that the response status code is 201 CREATED
        assert response.status_code == status.HTTP_201_CREATED

        # Make a reservation request
        data = {"cabin": "First Class", "members": 5}
        response = client.post(reverse('home-page'), data, content_type="application/json")
        response_list = [item for key, item in response.data.items()]

        # Check that the response status code is 201 CREATED
        assert response.status_code == status.HTTP_200_OK

        # Check that the response data contains the expected reservation details
        expected_data = ['First Class', 'Rs: 5000']
        for exp in expected_data:
            assert exp in response_list

    # Tests that the post method returns an error message when the requested cabin is not available
    @pytest.mark.django_db
    def test_post_method_returns_error_message_when_cabin_not_available(self, client):
        # Arrange
        request_data = {
            "cabin": "First Class",
            "members": 6
        }
        expected_response = {
            'message': 'The requested Cabin is not Available. Please provide correct Cabin from given option'
        }
        # Act
        response = client.post(reverse('home-page'), request_data, content_type="application/json")
        # Assert
        assert response.status_code == 400
        assert response.data == expected_response

    # Tests that the post method returns an error message when there are not enough seats available to accommodate
    @pytest.mark.django_db
    def test_post_method_returns_error_message_when_not_enough_seats_available(self, client):
        # Make a request to save cabin record
        data = {"name": "First Class", "capacity": 10}
        response = client.post(reverse('cabin-entry'), data, content_type="application/json")

        # Check that the response status code is 201 CREATED
        assert response.status_code == status.HTTP_201_CREATED
        # Arrange
        request_data = {
            "cabin": "First Class",
            'members': 30
        }
        expected_response = {
            'message': 'Sorry, there are not enough seats available to accommodate your family.'
        }

        # Make post request for making reservation
        response = client.post(reverse('home-page'), request_data, content_type="application/json")
        # Assert
        assert response.status_code == 400
        assert response.data == expected_response

