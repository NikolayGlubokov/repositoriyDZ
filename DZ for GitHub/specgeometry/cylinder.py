from math import *


class Cylinder:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def figure(self):
        return pi*self.a**2*self.b

    def info_figure(self):
        return f'Цилиндр:' \
               f'Радиус основания: '