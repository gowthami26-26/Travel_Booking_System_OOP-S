
# -*- coding: utf-8 -*-

# main.py
"""
Main program for Travel Booking System.

Steps:
1. Import TravelAgency from travel_agency.py
2. Create TravelAgency instance.
3. Display menu:
   - Add Customer
   - Make Booking
   - View Customer Bookings
   - Generate Report
   - Exit

Hint:
- Use input() for interaction.
- Wrap operations in try/except for clean error handling.
"""
from travel_agency import TravelAgency
from exceptions import CustomerNotFoundError

def main():
     agency = TravelAgency()
    
     while True:
        print("\n--- Travel Booking Menu ---")
        print("1. Add Customer")
        print("2. Make Booking")
        print("3. View Customer Bookings")
        print("4. Generate Report")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            name=input("Enter the name:")
            email=input("Enter customer email:")
            phone=input("Enter customer phone:")
            customer=agency.add_customer(name,email,phone)
            print(f"Customer created successfully! ID: {customer.customer_id}")
            
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            trip_name = input("Enter trip name: ")
            try:
                price = float(input("Enter price: "))
            except ValueError:
                print("Invalid price. Try again.")
                continue
            if customer_id in agency.customers:
                agency.make_booking(customer_id, trip_name, price)
            else:
                print(f"No customer found with ID {customer_id}")
             
        elif choice == "3":
            customer_id = input("Enter customer ID: ")
            try:
                agency.view_customer_bookings(customer_id)
            except CustomerNotFoundError as e:
                print(e)
                
             
              
        elif choice == "4":
            agency.generate_reports()
             
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    

if __name__ == "__main__":
    main()
