 # travel_agency.py
"""
TravelAgency class → manages customers and bookings.

Responsibilities:
- Add new customers
- Make bookings
- Link bookings to customers
- View bookings by customer
- Generate reports

💡 Hint:
- Use dictionaries {id: Customer} for customers.
- Maintain a list of all bookings.
"""

from customer import Customer
from booking import Booking
from exceptions import CustomerNotFoundError, BookingNotFoundError, DuplicateCustomerError, InvalidInputError

import utils


class TravelAgency:
    def __init__(self):
        self.customers = {}   # {customer_id: Customer}
        self.bookings = []    # list of Booking objects

    def add_customer(self, name, email, phone):
        """Add a new customer to the agency."""
        customer_id = utils.generate_id("CUST")
        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer
        print(f"Customer added: {customer}")
        return customer

    def make_booking(self, customer_id, trip_name, price):
        """Make a new booking for an existing customer."""
        if customer_id not in self.customers:
            raise CustomerNotFoundError(f"No customer found with ID {customer_id}")

        booking_id = utils.generate_id("BOOK")
        booking = Booking(booking_id, trip_name, price, status="Confirmed")

        self.bookings.append(booking)
        self.customers[customer_id].add_booking(booking)

        print(f"Booking added for customer {customer_id}: {booking}")
        return booking

    def view_customer_bookings(self, customer_id):
        """Display all bookings for a given customer."""
        if customer_id not in self.customers:
            raise CustomerNotFoundError(f"No customer found with ID {customer_id}")

        customer = self.customers[customer_id]
        if not customer.bookings:
            print(f"No bookings found for {customer_id}")
        else:
            print(f"\nBookings for {customer.name} ({customer_id}):")
            for booking in customer.bookings:
                print(f"Booking {booking.booking_id}: {booking.trip_name} - ₹{booking.price} ({booking.status})")


    def generate_reports(self):
        """Generate summary report for the agency."""
        total_bookings = len(self.bookings)
        total_revenue = sum(b.price for b in self.bookings if b.status == "Confirmed")
        active_customers = len(self.customers)

        print("Total Bookings:", total_bookings)
        print("Total Revenue: ₹", total_revenue)
        print("Active Customers:", active_customers)
