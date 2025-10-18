# -*- coding: utf-8 -*-
# report.py
"""
Reporting functions for Travel Booking System.

Functions:
- customer_report(customer)
- agency_summary(agency)
"""

def customer_report(customer):
    # Print all bookings of a customer
    print(f"Customer:{customer.name}({customer.email})")
    if not customer.bookings:
        print("No bookings found")
    else:
        for booking in customer.bookings:
            print(booking)
     

def agency_summary(agency):
    # Print total bookings and total revenue
    total_bookings = len(agency.bookings)
    total_revenue = sum(b.price for b in agency.bookings if b.status == "Confirmed")

    print("Agency Summary:")
    print("Total Bookings:", total_bookings)
    print("Total Revenue: ₹", total_revenue)
     

