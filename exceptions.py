# -*- coding: utf-8 -*-
# exceptions.py
"""
Custom exceptions for Travel Booking System.
"""

class CustomerNotFoundError(Exception):
    pass

class BookingNotFoundError(Exception):
    """Raised when a booking is not found."""
    pass

class InvalidInputError(Exception):
    """Raised when the input provided is invalid."""
    pass

class DuplicateCustomerError(Exception):
    """Raised when trying to add a customer that already exists."""
    pass