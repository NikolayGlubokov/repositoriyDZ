from specgeometry import circle, cylinder, rectangle
from random import randint


def homework34():
    n = int(input('Введите количество кругов: '))
    m = int(input('Введите количество прямоугольников: '))
    k = int(input('Введите количество цилиндров: '))

    circle_lst = []
    cylinder_lst = []
    rectangle_lst = []

    for i in range(n):
        i = circle.Circle(randint(0,20))
        circle_lst.append(i)

    for i in circle_lst:
        print(f'Длина окружности: {i.perimeter()}')

    for i in circle_lst:
        print(f'Площадь круга равна: {i.area()}')

    for i in range(k):
        i = rectangle.Rectangle(randint(0,20), randint(0,20))
        rectangle_lst.append(i)

    for i in rectangle_lst:
        print(i.perimeter())

    for i in range(m):
        i = cylinder.Cylinder(randint(0,20),randint(0,20))
        cylinder_lst.append(i)

    for i in cylinder_lst:
        print(f'Площадь круга равна: {i.area_circle()}')
        print(f'Объём цилиндра равен: {i.value()}')

    def max_area():
        v1=[]
        for i in range(len(circle_lst)):
            v1.append(circle_lst[i].area())
        v2=max(v1)
        for i in range(len(circle_lst)):
            if v2==circle_lst[i].area():
                return f'Радиус: {circle_lst[i].r}'


    print(f'Окружность с наибольшей площадью:', max_area())
    print(f'Прямоугольник с наименьшим периметром:', min([rectangle_lst[i].perimeter() for i in range(len(rectangle_lst))]))
    print(f'Средний объём всех цилиндров:', sum([cylinder_lst[i].value() for i in range(len(cylinder_lst))])/len(cylinder_lst))

# cir1=circle.Circle(20)
# cir1.info()
# print(cir1.area())
# print(cir1.perimeter())
# cil1=cylinder.Cylinder(20,50)
# cil1.info()
# print(cil1.area())
# print(cil1.value())
# rec1=rectangle.Rectangle(30, 6)
# rec1.info()
# print(rec1.area())
# print(rec1.perimeter())

# homework35()
homework34()
