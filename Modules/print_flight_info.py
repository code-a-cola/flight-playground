#!/usr/bin/env python3

from Modules.print_seating import print_seating
from Modules.print_cards import print_cards
from Modules.print_totals import print_totals

def print_flight_info(flights):
    for flight in flights:
        print_seating(flight)
        print_cards(flight)
        print_totals(flight)