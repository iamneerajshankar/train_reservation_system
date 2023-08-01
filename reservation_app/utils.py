"""
Contains the util method
"""
import uuid


class BaseUtilClass:

    """
    Calculate and verify the seat availability based cabin and members count
    """
    @staticmethod
    def check_seat_availability(available_seats, family_members):
        # Check if there are enough seats available in the same cabin to accommodate the family.
        # Return True if enough seats are available, else False.
        if available_seats >= family_members:
            return True
        return False

    """
    Returns the seat to be reserved for booking
    """
    @staticmethod
    def select_seats(preferred_cabin, family_members):
        # Retrieve seat numbers for the selected cabin class.
        # Determine suitable arrangement to accommodate the family members.
        # Return the list of selected seat numbers.
        selected_seats = []
        for seat_num in range(1, family_members + 1):
            selected_seats.append(f"{preferred_cabin[0]}{seat_num}")
        return selected_seats

    """
    Return the the reservation details
    """
    @staticmethod
    def send_reservation_details(cabin_class, selected_seats):
        # calculate and display the total fare for the reservation.
        total_fare = 1000 * len(selected_seats)
        reservation_detail = {
            "reservation_id": str(uuid.uuid4()),
            "selected_cabin": cabin_class,
            "selected_Seat": selected_seats,
            "fare": "Rs: " + str(total_fare)
        }

        return reservation_detail
