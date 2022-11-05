#!/usr/bin/env python3

def card_printer(passenger, seat, flight_number, registration, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Registration: {registration}" \
             f" Aircraft: {aircraft}" \
             f" Code: {registration}:{flight_number}:{seat}" \
             " |"

    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    lines = [banner, border, output, border, banner]

    card = "\n".join(lines)

    print(card)
    print()