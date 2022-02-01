from random import randint #Задание произвольного массива
d=int(input('Введите количество: '))
n=[]
for i in range(d):
    sls = randint(0, 10)
    n.append(sls)
print(n)
c=0

for i in range(len(n)):#Задание №1 - четные индексы
    if i % 2 == 0:
        print(n[i])

for i in range(1, len(n)): #Задание №2 - выведение большего элемента. Однако, данный алгоритм проходит по всему списку, а не делит его на пары, как это в примере
    if n[i] > n[i - 1]:
        print(n[i], end=' ')
print()

p=0 #Задание №3 - выведение одиночных элементов из списка
d=[]
for i in range(len(n)):
    c=n[i]
    k=0
    for j in n:
        if c == j:
            k+=1
    if k==1:
        d.append(n[i])
print(d)