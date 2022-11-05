#!/user/bin/env python3

from Modules.Classes.Flight import Flight
from Modules.Classes.Boing747 import Boing747
from Modules.Classes.AirbusA319 import AirbusA319

from Modules.print_flight_info import print_flight_info

flights = ( Flight("NA06012", Boing747("747-8F")), Flight("NA06012", AirbusA319("G-EUPT")) )

a, b = flights

a.allocate_seat("12A", "Guido Van Rossum")
a.allocate_seat("12B", "Rasmus Lerdoff")
a.allocate_seat("12D", "Egor Plethroff")
a.allocate_seat("14F", "Hale Walker")

a.reallocate_seat("12B", "12C")
a.reallocate_seat("12D", "21A")

b.allocate_seat("12A", "Guido Van Rossum")
b.allocate_seat("12B", "Rasmus Lerdoff")
b.allocate_seat("12D", "Egor Plethroff")
b.allocate_seat("14F", "Hale Walker")

b.reallocate_seat("12B", "12C")
b.reallocate_seat("12D", "21A")

print_flight_info(flights)