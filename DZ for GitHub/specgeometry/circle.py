from math import *


class Circle:
    def __init__(self, r):
        self.r = r

    def info(self):
        print(f'Радиус круга: {self.r}')

    def area(self):
        return pi*self.r**2
