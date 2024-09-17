class Circle:
    def pi(self):
        return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        # woah, that's a big number! (shocking)

    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.pie = self.pi() # called pie lol

my_new_circle = Circle(5)

print("Radius: " + my_new_circle.radius)
print("Diameter: " + my_new_circle.diameter)
print("Pi (fn): " + my_new_circle.pi())
print("Pi (var): " + my_new_circle.pie)