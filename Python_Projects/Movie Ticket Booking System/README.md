# Movie Ticket Booking System

A simple Python-based movie ticket booking system built using fundamental programming concepts like variable manipulation, dynamic user input handling, and conditional logic (`if-elif-else`).

## Features
- **Dynamic Input Tracking:** Collects user information such as age, student status, weekend bookings, and VIP preferences.
- **Mutually Exclusive Discounts:** Prevents overlapping offers by ensuring users under 15 get a child discount, while older students get a dedicated student discount.
- **Surcharges & Extras:** Automatically applies weekend premiums and VIP seat charges based on responses.

## Pricing Logic
- **Base Ticket Price:** ₹150
- **Discounts:**
  - Child (Age < 15): 10% off base price
  - Student (Age 15+): 15% off base price
- **Additional Charges:**
  - Weekend Surcharge: +₹100
  - VIP Ticket Premium: +₹250

## How to Run
1. Ensure you have Python installed on your system.
2. Save the code to a file named `ticket_booking.py`.
3. Open your terminal or command prompt and execute:
   ```bash
   python ticket_booking.py
   ```
4. Follow the interactive screen prompts to calculate your total ticket cost.
