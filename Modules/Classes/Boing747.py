#!/usr/bin/env python3

from Modules.Classes.Aircraft import Aircraft

class Boing747(Aircraft):


    def __init__(self, registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def model(self):
        return "Boing 747"


    def seating_plan(self):
        return range(1,56), "ABCDEFGHJK"