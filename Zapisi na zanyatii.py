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
# # e={randint(0, 10) for i in range(randint(1,3))}
# # r={randint(0, 10) for i in range(randint(1,3))}
# # t={andint(0, 10) for i in range(randint(1,3))}
# # y={randint(0, 10) for i in range(randint(1,3))}
# #
# # s=q|w|e|r|t|y
# # print(s)
# # print(len(s))
# # print(min(list(s)))
# # print(max(list(s)))
# x = dict(a=1, b=2)
# y = dict(b=4, c=6)
# z=x.copy()
# z.update(y)
# b=x|y
# print(z)
# print(b)
# #     x1=['i3',9, 4500],
# #     x2=['i5', 3,10000],
# #     x3=[ 'i7', 6,2000],
# #     x4=[ 'amd',8,3500],
# #     x5=['pentium',5,8000]
# # )
# # for i in a:
# #     print(i, a[i],'\n')
# # c=input("Zamena")
# # d = int(input('kol-vo'))
# # for i in a:
# #     for j in i:
# #         if i==c:
# #             a[i][1]=d
# #
# #     print(a)
#
# # s = 1
# # for i in a:
# #     s *= a[i]
# #
# # print(s)
# #
# # a= {i: input('Введите название овоща') for i in range(1, 5)}
# # print(a)
# # b=int(input("Какой элемент вы хотите удалить? "))
# # del a[b]
# # print(a)
#
# a = dict(John=dict(N=randint(1000,5000), S=randint(1000,5000), E=randint(1000,5000), W=randint(1000,5000)),
#          Tom=dict(N=randint(1000,5000), S=randint(1000,5000), E=randint(1000,5000), W=randint(1000,5000)),
#          Anna=dict(N=randint(1000,5000), S=randint(1000,5000), E=randint(1000,5000), W=randint(1000,5000)),
#          Fiona=dict(N=randint(1000,5000), S=randint(1000,5000), E=randint(1000,5000), W=randint(1000,5000)))
# for i in a:
#     print(i)
#     for y in a[i]:
#         print('\t', y, ':', a[i][y], sep='')
#
# l = input('Введите имя продавца: ')
# p = input('Введите регион: ')
#
# a[l][p]=input('Введите нужное значение: ')
#
# for i in a:
#     print(i)
#     for y in a[i]:
#         print('\t', y, ':', a[i][y], sep='')

# a = {'один': 1, "два": 2, 'три': 3, 'четыре': 4}
# b = {{value: value for key ,value   in a.items()} if value<=2}
# print(b)
#
# lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# a = {}
# p = None
# for i in lst:
#     if type(i) is str:
#         a[i] = []
#         p = i
#     else:
#         a[p].append(i)
# print(a)

# a = ['January', 'February', 'March']
# b = [52000, 51000, 48000]
# c = [46800, 45900, 43200]
# for prod, prib, m in zip(b,c,a):
#     print("obschaya pribil v", m, '=', prod-prib)


# def funct(student,*a):
#     print('Student name:', student)
#     for i in range(len(a)):
#         if i  < (len(a)-1):
#             print(i, end=', ')
#         if i == (len(a)-1):
#             print(i, end=' ')
#     print()
#
# def funct(student, *a):
#     print(student, end=' ')
#     print(*a, sep=', ')
#     print()
#
#
# funct('Igor', 2, 3, 4, 5, 6, 7, 8, 9)
# funct('Nick', 3, 6, 1, 9, 5)

# while (number > 0):
#     remainder = number % 10
#     revs_number = (revs_number * 10) + remainder
#     number = number // 10
# def revrs(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def funct(*a, only_odd=False):
#     res = []
#     for i in a:
#         if not only_odd or (only_odd and i % 2 == 0):
#             res.append(revrs(i))
#     return res
#
#
# print(funct(235, 75464, 725435, 33, 78, 972))
# print(funct(235, 75464, 725435, 33, 78, 972, only_odd=True))
my_dict={'one':'first'}


def db(**args):
    my_dict.update(args.items())
    return my_dict

print(db(k56=52, two=33))
print(db(g5=52, j6=33))


