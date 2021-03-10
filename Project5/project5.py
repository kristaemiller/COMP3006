#Krista Miller
#COMP 3006

# *** PART 1: SHAPE CLASSES ***
# Create a shape class to be the basis for later classes extending from it.
# Include any variables that you believe are universal to all shapes.
# Create an area method, and any other methods that are universal to all shapes
# Create a class for each of the following shapes including the fundamental variables needed in each shape.

PI= 3.14
import math

class Shape:
    #constructor
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        return (int(self.height * self.base))
    def perimeter(self):
        return (int(self.height*2 + self.base*2))
    def __str__(self):
        return f'Shape area = {self.area()} units squared, ' \
               f'perimeter = {self.perimeter()} units'

class Parallelogram(Shape):
    def __str__(self):
        return f'Parallelogram shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.perimeter()} units'

class Rectangle(Parallelogram):
    def __str__(self):
        return f'Rectangle shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.perimeter()} units'

class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)
    def __str__(self):
        return f'Square shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.perimeter()} units'

class Triangle(Shape):
    def __init__(self, height, base, side2, side3):
        super().__init__(height, base)
        self.height = height
        self.base = base
        self.side2 = side2
        self.side3 = side3
    def area(self):
        return (0.5 * self.base) * self.height
    def perimeter(self):
        return(self.base + self.side2 + self.side3)
    def __str__(self):
        return f'Triangle shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.perimeter()} units'

class Rhombus(Parallelogram):
    def __init__(self, diagonal1, diagonal2, base):
        super().__init__(base, base)
        self.base = base
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def area(self):
        return ((self.diagonal1 * self.diagonal2) / 2)
    def __str__(self):
        return f'Rhombus shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.perimeter()} units'

class Polygon(Shape):
    """regular polygon with equal sides length. the apothem is a line segment that
    joins the polygon's center to the midpoint of any side that is perpendicular
    to that side."""
    def __init__(self, numsides, apothem, sidelength):
        super().__init__(apothem, sidelength)
        self.numsides = numsides
        self.sidelength = sidelength
        self.apothem = apothem
    def area(self):
        perimeter = (self.numsides * self.sidelength)
        return ((perimeter * self.apothem) / 2)
    def __str__(self):
        return f'Regular polygon shape: area = {self.area()} units squared, ' \
               f'perimeter= {self.numsides* self.sidelength} units'

class Pentagon(Polygon):
    def __init__(self, apothem, sidelength):
        super().__init__(5, apothem, sidelength)
        self.sidelength = sidelength
        self.apothem = apothem
    def __str__(self):
        return f'Pentagon shape: area = {self.area()} units squared, ' \
               f'perimeter= {(self.numsides* self.sidelength)} units'

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius,radius)
        self.radius = radius
    def area(self):
        return ((PI * self.radius**2))
    def circumference(self):
        return round((2*PI*self.radius), 2)
    def __str__(self):
        return f'Circle shape: area = {self.area()} units squared, ' \
               f'circumference= {self.circumference()} units'
#
class Oval(Shape):
    def __init__(self, majoraxis, minoraxis):
        super().__init__(majoraxis, minoraxis)
        self.majoraxis = majoraxis
        self.minoraxis = minoraxis
    def area(self):
        return ((PI * self.majoraxis * self.minoraxis))
    def circumference(self):
        return round(((2*PI* math.sqrt(0.5*self.majoraxis**2 + 0.5*self.minoraxis**2))),2)
    def __str__(self):
        return f'Oval shape: area = {self.area()} units squared, ' \
               f'circumference= {self.circumference()} units'

# *** PART 2: ZIP FUNCTION ***
# Using a list of Suits and Values, take advantage of the zip function to create a
# list of tuples of a standard set of cards

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(s, v) for s, v in zip(suits, values) for v in values]

#testing deck
# print(deck)
# print(len(deck))

#testing shapes
# rhombus= Rhombus(8,7,6)
# print(rhombus)
# triangle= Triangle(7,5,3,4)
# print(triangle)
# pentagon= Pentagon(7,9)
# print(pentagon)
# circle= Circle(2)
# print(circle)
# oval= Oval(3,4)
# print(oval)
# polygon= Polygon(4,3,2)
# print(polygon)
# square= Square(3)
# print(square)
# rectangle= Rectangle(4,5)
# print(rectangle)
