#!/usr/bin/env python3

from Modules.Classes.Aircraft import Aircraft

class AirbusA319(Aircraft):


    def model(self):
        return "Airbus A319"


    def seating_plan(self):
        return range(1,23), "ABCDEF"