#!/usr/bin/env python3

class Aircraft:


    def num_rows(self):
        rows, row_seats = self.seating_plan()
        return len(rows)


    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


    def num_seats_per_row(self):
        rows, row_seats = self.seating_plan()
        return len(row_seats)