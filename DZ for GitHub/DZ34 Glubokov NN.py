from specgeometry import circle, cylinder, rectangle


def homework35():
    n = int(input('Введите количество кругов: '))
    # m = int(input('Введите количество прямоугольников: '))
    # k = int(input('Введите количество цилиндров: '))
    circle_lst = []
    cylinder_lst = []
    rectangle_lst = []

    for i in range(n):
        i = circle.Circle(int(input('Введите радиус окружности: ')))
        circle_lst.append(i)

    for i in circle_lst:
        print(i.area())
# cir1=circle.Circle(20)
# cir1.info()
# cil1=cylinder.Cylinder(20,50)
# cil1.info()
# rec1=rectangle.Rectangle(30, 6)
# rec1.info()

homework35()
