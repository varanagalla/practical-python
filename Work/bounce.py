# bounce.py
#
# Exercise 1.5

"""
A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints
a table showing the height of the first 10 bounces.
"""

fell_from_height = 100 # meters
bounce_back_fraction = 3/5
no_of_bounces = 10

while no_of_bounces > 0:
    fell_from_height *= bounce_back_fraction
    fell_from_height = round(fell_from_height, ndigits = 4)
    print(no_of_bounces, fell_from_height)
    no_of_bounces -= 1
