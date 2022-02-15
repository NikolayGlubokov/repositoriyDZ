from random import randint

# 
# def check_password(n, even=True):
#     sum = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             sum += cur_digit
#         if not even and cur_digit % 2 != 0:
#             sum += cur_digit
#         n //= 10
# 
#     return sum
# 
# 
# print(check_password(754622, even=False))
# 
# 
# def display_info(name, age):
#     print('Name:', name, "\n Age:", age, "\n")
# 
# 
# display_info('Ira', 23)
# display_info(age=23, name='Ira')
# display_info('Igor', 23)
# 
# 
# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
# 
# 
# print(func(1))
# print(func(1))
# print(func(1))
# a = 5
# b = 5
# print(id(a))
# print(id(b))
# 
# lt = [1, 2, 3, 4]
# lt1 = [1, 2, 3, 4]
# print(id(lt))
# print(id(lt1))
# print(lt == lt1)
# print(lt is lt1)
# 
# 
# def add_number(n):
#     print('Vnutri funkcii: ', n, '=', id(n))
#     n += 1
#     print('Posle prisvoeniya:', n, '=', id(n))
#     return n
# 
# 
# x = 1
# print(x, '=', id(x))
#
# x = [randint(0, 9) for i in range(10)]
# print(x)
#
#
# def func(s):
#     ls = []
#     for i in s:
#         if i not in ls:
#             ls.append(i)
#
#     return tuple(reversed(ls))
#
#
# print(func(x))
# q={randint(0, 10) for i in range(randint(1,3))}
# w={randint(0, 10) for i in range(randint(1,3))}
# e={randint(0, 10) for i in range(randint(1,3))}
# r={randint(0, 10) for i in range(randint(1,3))}
# t={andint(0, 10) for i in range(randint(1,3))}
# y={randint(0, 10) for i in range(randint(1,3))}
#
# s=q|w|e|r|t|y
# print(s)
# print(len(s))
# print(min(list(s)))
# print(max(list(s)))
x = dict(a=1, b=2)
y = dict(b=4, c=6)
z=x.copy()
z.update(y)
b=x|y
print(z)
print(b)
#     x1=['i3',9, 4500],
#     x2=['i5', 3,10000],
#     x3=[ 'i7', 6,2000],
#     x4=[ 'amd',8,3500],
#     x5=['pentium',5,8000]
# )
# for i in a:
#     print(i, a[i],'\n')
# c=input("Zamena")
# d = int(input('kol-vo'))
# for i in a:
#     for j in i:
#         if i==c:
#             a[i][1]=d
#
#     print(a)

# s = 1
# for i in a:
#     s *= a[i]
#
# print(s)
#
# a= {i: input('Введите название овоща') for i in range(1, 5)}
# print(a)
# b=int(input("Какой элемент вы хотите удалить? "))
# del a[b]
# print(a)
