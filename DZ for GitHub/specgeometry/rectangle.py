class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def info(self):
        print(f'Ширина прямоугольника: {self.a}\n'
              f'Длина прямоугольника: {self.b}')