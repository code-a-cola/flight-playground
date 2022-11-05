#!/usr/bin/env python3

def print_totals(flight):
    aircraft = flight.aircraft()
    print(f"Nunber of Rows: {aircraft.num_rows()}")
    print(f"Nunber of Seats: {aircraft.num_seats()}")
    print(f"Nunber of Seats p/ Row: {aircraft.num_seats_per_row()}")
    print(f"Available Seats: {flight.num_available_seats()}")
    print()