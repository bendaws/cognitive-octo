# geometry.py - a bunch of shapes
# (C) copyright 2024 Ben Daws
# gnu gpl v3

class circle:
    def pi(self):
        return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        # woah, that's a big number! (shocking)

    def area(self):
        return self.pi() * self.radius ^ 2

    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.pie = self.pi() # called pie lol

class rectangle:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

class triangle:
    def area(self):
        return (self.width * self.height) / 2

    def __init__(self, width, height):
        self.width = width
        self.height = height