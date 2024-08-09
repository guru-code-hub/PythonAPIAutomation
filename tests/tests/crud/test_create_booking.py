import allure
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking id...")
    @allure.description("Creating a booking from the payload and verify that booking id...")
    def test_create_booking_positive(self):
        pass
