from math import *
from specgeometry import rectangle


class Cylinder(rectangle.Rectangle):
    def __init__(self, r, b):
        self.r=r
        super().__init__(self, b)

    def info(self):
        print(f'Радиус цилиндра: {self.r}\n'
              f'Высота цилиндра: {self.b}')

