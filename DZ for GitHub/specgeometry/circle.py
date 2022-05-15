from math import *


class Circle:
    def __init__(self, r):
        self.r = r

    def info(self):
        print(f'Радиус круга: {self.r}')

    def area(self):
        return round(pi*self.r**2,2)

    def perimeter(self):
        return round(2*pi*self.r,2)


