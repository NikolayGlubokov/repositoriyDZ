from random import randint

low_line = '-------------'
print(low_line * 8)
print('Задание №1')
n=int(input('Введите размерность матрицы: '))
matrix = [[randint(0, 100) for j in range(n)] for i in range(n)]
c = 100011111111111
d = -11111111111111
e = 100000000000
s = 0
for row in matrix:
    l = 0
    for col in row:
        if col < c:
            c = col
        if col > d:
            d = col
        print(col, end='\t\t')
        if l == s and e >= col:
            e = col
        l += 1
    print()
    s += 1
# print("Минимальное значение всего списка", c)
# print("Максимальное значение всего списка", d)
print("Минимальное значение главной диагонали равно", e)

print(low_line * 8)
print('Задание №2')

sup_matrix = [randint(-10, 0) for i in range(n)]
print('Имплантируемый список: ', sup_matrix)
for row in range(len(matrix)):
    if row % 2 == 0:
        for col in range(len(matrix[row])):
            print(sup_matrix[col], end='\t\t')
    else:
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='\t\t')
    print()

print("Начал разбираться")