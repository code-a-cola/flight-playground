#!/usr/bin/env python3

class Flight:


    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()

        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def aircraft(self):
        return self._aircraft


    def seating(self):
        return self._seating


    def allocate_seat(self, seat, passenger):
        row, letter = self.parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger


    def reallocate_seat(self, from_seat, to_seat):
        from_row, from_letter = self.parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self.parse_seat(to_seat)

        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]

        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)


    def parse_seat(self, seat):
        rows, seats = self._aircraft.seating_plan()

        letter = seat[-1]

        if letter not in seats:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        return row, letter


    def print_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self.passenger_seats()):
            card_printer(passenger, seat, self._number, self._aircraft.registration(), self._aircraft.model())


    def passenger_seats(self):
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for letter in seats:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


    # def passengers(self):
    #     return [[f"{idx}{allocation}", row[allocation]]
    #             for idx, row in enumerate(self._seating)
    #             for allocation in row if (row is not None and row[allocation] is not None)]