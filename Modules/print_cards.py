#1/user/bin/env python3

from Modules.card_printer import card_printer

def print_cards(flight):
    flight.print_boarding_cards(card_printer)