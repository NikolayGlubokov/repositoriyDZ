from math import *
from random import *
import re
import time

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
# my_dict={'one':'first'}


# def db(**args):
#     my_dict.update(args.items())
#     return my_dict
#
# print(db(k56=52, two=33))
# print(db(g5=52, j6=33))

# from math import *
# from random import *
#
#
# def rhombus(**a):
#     b = list(a.values())
#     s = (b[0] * b[1]) / 2
#     return s
#
#
# def squared(**a):
#     b = list(a.values())
#     s = b[0] ** 2
#     return s
#
#
# def trapezoid(**a):
#     b = list(a.values())
#     s = ((b[0] + b[1]) * b[2]) / 2
#     return s
#
#
# def circle(**a):
#     b = list(a.values())
#     s = (b[0] ** 2) * pi
#     return s
#
#
# def funct(figure_type='unknown', **args):
#     if figure_type == 'rhombus':
#         print(rhombus(**args))
#     elif figure_type == 'squared':
#         print(squared(**args))
#     elif figure_type == 'trapezoid':
#         print(trapezoid(**args))
#     elif figure_type == 'circle':
#         print(circle(**args))
#     else:
#         print('Invalid data')
#
#
# funct(figure_type='rhombus', d1=10, d2=8)
# funct(figure_type='squared', a=5)
# funct(figure_type='trapezoid', a=12, b=3, h=6)
# funct(figure_type='circle', r=18)
# funct(figure_type='unknown', a=5, b=2, c=3)
#
#
# def outer(n):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         return n, s
#
#     return inner
#
#
# res = outer('Москва')
# print(res())
# print(res())
# res2 = outer('Сочи')
# print(res2())
# print(res2())
# print(res())
# #
# add5 = outer(5)
# print(add5(10))
# print(outer(5)(19))
#
# print((lambda x: (lambda y: (lambda z: x + y + z)))(4)(6)(10))
#
# lst = [1,2,3,4,5]
# print(max(lst))
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
# d = {
#     1: lambda x: print(pi * x ** 2),
#     2: lambda x, y: print(x * y),
#     3: lambda a, b, h: print((a + b) * h / 2)
# }
# d[1](12)
# d[2](2, 5)
# d[3](4, 7, 10)
# print((lambda x, y, z: min(x, y, z))(6, 2, 18))
# b = ['madam', 'adam', 'seves', 'retem', 'abbadon']
# print(b)
# print(list(filter(lambda x: x == x[::-1], b)))
# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func super_func')
#     print(func())
#
#
# super_func(hello)
#
#
# def hello2():
#     return 'Hello, i am func "hello"'
#
#
# test = hello2
# print(test())

# def my_decorator(func):  # dekoriruysaa funczia
#     i = 0
#
#     def func_wrapper():
# #         nonlocal i
# #         i += 1
# #         func()
# #         print('вызов функции:', i)
# #
# #     return func_wrapper
# #
# #
# # @my_decorator  # decorator
# # def func_test():  # dekoriruemaya func
# #     print('Hello')
# #
# #
# # func_test()
# # func_test()
# # func_test()
# # #
# # # test=my_decorator(func_test)
# # # test()
# def func1(x):
#     def func2(y):
#         s = x * y
#         return s
#
#     return func2
#
#
# res = func1(3)
# print(res(20))
# print(res(15))
# res = func1(10)
# print(res(15))
# print(res(15))
#  def typed(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# #
# # @typed(int, int, int)
# # def typed_fn(x, y, z):
# #     return x * y * z
# #
# #
# # @typed(str, str, str)
# # def typed_fn2(x, y, z):
# #     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# # print(typed_fn(3, 4, 5))
# # # print(typed_fn(3, 4, "Hello"))
# # print(typed_fn2("Hello, ", "world", "!"))
# # print(typed_fn2("Hello, ", "world", 2))
# print(typed_fn3("Hello, ", "world!  ", z=5))
# 
# def decor(tx=None, dec_text=""):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end="")
#             func(*args)
# 
#         return wrap
# 
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
# 
# 
# @decor
# def hello_world2(text):
#     print(text)
# 
# 
# hello_world2("Hi!")
# 
# 
# @decor(dec_text="Hello, ")
# def hello_world(text):
#     print(text)


# # hello_world("world!")
# str1=' Я изучаю Nuthon. Мне нравится Nuthon. Nuthon мой любимый язык программирования'
# lst=''
# for i in range(len(str1)):
#     if 'N' == str1[i]:
#         lst+='P'
#     else:
#         lst+=str1[i]
#
# print(lst)

# s='Test string for me'
# s2=[]
# for i in s:
#     s2.append(ord(i))
# print(s2)
# s2=[int(sum(s2)/len(s2))]+s2
# print(s2)
# s2+=[x for x in [ord(x) for x in (input('->'+' '[:3]))] if x not in s2]
# print(s2)
# if s2[-1] in s2[:-1]:
#     print(s2.count(s2[-1])-1)

# a = 97
# b = 122
# for x in range(a, b + 1):
#     print(chr(x), end=' ')
# STEST = 7
# LONGST = 10
# mingAske = 33
# maxAske = 122
#
#
# def random_password():
#     random_length = randint(STEST, LONGST)
#     res=''
#     for i in range(random_length):
#         random_char=chr(randint(mingAske,maxAske))
#         res+=random_char
#     return res
#
# print(random_password())
# print(random_password())
# print(random_password())
# print(random_password())


# s = 'hello, WORLD! I am learning Python'
# d = list(s)
# print(s[:5])
# print(s)
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.count('o'))
# print(s.find('lo'))
# print(list(s))
# print(str(d))

# s = 'odin dwa'
# s2 = s[s.find(' '):] + ' ' + s[:s.find(' ')]
# print(s2)
# s='sdfsdfge332gg3'
# digits=[]
# for x in s:
#     if '0123456789'.find(x)!=-1:
#         digits.append(x)
#     else:
#         pass
# # print(digits)
# print(dir(str))
# s='123125425234'
# print(s.index('3'))


# def func(e):
#     r = e.count(' е') + e.count('Е')
#     print(r)
#
#
# func(c)

# c = 'Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели'
# g = '11 23 44 55 23 22'
# h = '23'
# b = ''
# print(g.index('23'))
# print(len(h))
# print(g.find(h))
# while len(g) != 0:
#     if g.find(h) != -1:
#         b = b + g[:g.index(h)]
#         g = g[g.index(h) + len(h):]
#     else:
#         b += g
#         g = ''
#
# print(b)
#
#
# c = '''примерная строка для
# формирования в
# список по
# начальным
# символам'''
# x = 'c'
# d = []
# while True:
#     if c.find(' ')!=-1:
#         d.append(c[:c.find(' ')])
#         c=c[c.find(' ')+1:]
#     else:
#         d.append(c)
#         break
#
# print(d)
# c=0
# for i in range(len(d)):
#     if '\n' in d[i]:
#         print(d[i])
# for i in range(len(d)):
#     if (d[i][0]=='с' or d[i][0]=='С') and len(d[i])>2:
#         c+=1
#
# print(c)

# c = 'I am learning Python. hello, World!'
# c = c[:c.find('h')] + c[c.rfind('h') + 1:]
# print(c)
# print('abc123'.isalnum())
# print('abc$123'.isalnum())
# print(' '.isalnum())
# print('abcABC'.isalpha())
# print('abc5ABC'.isalpha())
# print('12345'.isdigit())
# print('abc5ABC'.isdigit())
# print('abc'.isidentifier())
# print('1abc'.isidentifier())
# print('abc'.isidentifier())
# print('abc'.islower())
# print('Abc'.islower())
# print('ab$c'.islower())
# print('\t\n'.isspace())
# print('The Apple'.istitle())
# print('ABC'.isupper())

# print('py'.center(10,'-'))
# print('py'.center(9,'-'))
# print('py'.center(2,'-'))
# print('py     '.rstrip())
# print('py     ')
# print('     py'.lstrip())
# print('        py     ')
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$:'.rstrip(':$.'))

# print('https://www.python.org'.lstrip('/:pths').rstrip('org.'))
# #
# #
# print('     py    '.strip())
# print('www.python.org/'.strip('/org.w'))

# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
#
# print(s.replace('Nython','Python',2))

# s='-'
# seq=('a','b','c')
# print(s.join(seq))
# print('__'.join(['1','2']))
# print(':'.join('Hello'))
#
# print('Строка разделенная пробелами'.split())
# print('www.python.org'.split('.'))
# print('www.python.org'.split('.',1))
# a = input('Введите ФИО')
# a = a.split()
# # print(a[0],a[1][0]+'.'+ a[2][0]+'.')
# print('www.python.org'.split('.'))
# print('www.python.org'.rsplit('.',1))
# # print('*'.join((input('->').split())))!!!!!!
#
#
# s = ' Я ищу совпадения в 2021 году. И я их обязательно найду'
# reg = r'20*'
# print(s)
# print(re.findall(reg, s))  # spisok vseh sovpadeniy
# print(re.findall('12', s))
# # print(re.search(reg, s))#pervoe sovpadenie
# # print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg,s)) #poisk s nachala

# print(re.split(reg, s, 1))
# print(re.sub(reg, '!', s)) #zamena na novoe znachenie
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта'
# # reg = r'[12][0-9][0-9][0-9]'
# reg = r'[А-ЯЁа-яё.]'
# print(re.findall(reg, s))
# s = 'Еда, беду, победа'
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s))
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта'
# reg = r'[0-2]'
# print(re.findall(reg, s))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09"
# reg=r'[0-2][0-3]:[0-5][0-9]'
# # print(re.findall(reg, s))
# print('https://github.com/Helen-prog/Python112/blob/master/112.py     https://disk.yandex.ru/d/rYQJzQvVllTQtw/17')
# d = 'Цифры: 7, +17,-42, 0013, 0.3'
# print(re.findall(r'[+-]?[\d.]+',d))

# s='05-03-1987 # дата рождения'
#
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s)))

# st = 'autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r'\w+\s*=\s*[^;]*'
# print(re.findall(reg, st))
# print(st.split(';'))
# s1 = 'МИ Д - Министерство иностранных дел, ГЭС - гидроэлектростанция, ФСБ - федеральная служба безопасности'
# reg1 = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]*'
# print(re.findall(reg1, s1))
# s='+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg=r'\+?7[0-9]{10}'
# print(re.findall(reg,s))
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта'
# #reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))
#
# print(re.findall(r'\w+','12 + й'))
# print(re.findall(r'\w+','12 + q', flags=re.ASCII))

# s='hello world'
# print(re.findall(r'\w\+',s,flags=re.DEBUG))


# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта'
# reg = r'я'
# print(re.findall(reg, s,flags=re.IGNORECASE))
# text = """
# {
# "one":1,
# "two":2,
# "three":3
# }
# """
# print(re.findall(r'one.\w+', text,flags=re.DOTALL))
# print(re.findall(r'one$', text,flags=re.MULTILINE))
# print(re.findall(r'^["\w+]+', text))
# print(re.findall(r'^["\w+]+', text, flags=re.MULTILINE))
# print(re.findall("""
# [a-z_.-]+# part1
# @
# [a-z_.-]+#part2
# """,'tes_t@mail.ru',flags=re.VERBOSE))
#
# text = """Python,
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, flags=re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Py'))
# print(validate_name('@Python_master#$%#$%#$%'))
#
# text2='123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3-67@i.ru 1login@ru.name.ru'
# reg=r'[\w.-]+@[\w.-]+[\w]{2,3}'
# print(re.findall(reg,text2))

# text3='<body> Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>',text3))
#
# text3='<body> Пример жадного соответствия регулярных выражений</body>'
# print(re.search('<.*?>',text3).group())

# text = "Python (в русском языке распространено название пито́н[16] или пайтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической типизацией и автоматическим управление памятью[18][19]."
# reg = r'\[.*?]'
# print(re.findall(reg,text,flags=re.MULTILINE))

# s = 'Пётр, Ольга и Виталий отлично учатся!'
# reg = r"Пётр|Ольга|Виталий"
# print(re.findall(reg, s))

# s='int=4,float=4.0, double=8.0f'
# #reg=r'\w+\s*=\s*\d[.\w+]*'
# # #reg=r'(int|float)\s*=\s*\d[.\w+]*'
# # reg=r'((int|float)\s*=\s*\d[.\w+]*)'
# print(re.findall(reg,s))

# s='World2016, PS6, AI5'
# reg=r'([a-z]+)(\d*)'
# reg1=r'([a-z]+\d*)'
# print(re.findall(reg,s, re.I))
# print(re.findall(reg1,s, re.I))
# s = '127.0.0.1'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s, re.I))
# s = '28-08-2021'
# reg=r'([0][1-9]|[0-2][0-9]|[0-3][0-1])-([0-1][0-2]|[0][1-9])-(19[0-9][0-9]|20[0-2][0-2])'
# reg1=r'\s'
# print(re.findall(reg,s))
# print(re.split(reg1,s))
# s = 'Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта'
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m=re.search(reg,s)
# print('Найдена строка: ', m[0])
# print('Найдена строка: ', m[1])
# print('Найдена строка: ', m[2])
#
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))
#
# s='<p> Изображение <img src="bg.jpg"> - фон страницы </p>'
#
# reg=r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg, s))
#
# reg2=r'<img\s+[^>]*src=(?P<q>[\'"])(.+)\(?P=q)>'
# print(re.findall(reg2, s))
#
# # s = 'Самолёт прилетает 10/23/20221. Будем рады вас видеть после 10/24/2021'
# # reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.sub(reg, r":\2.\1.\3", s))
# s='google.com and google.ru'
# reg=r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))


# def elevator(n):
#     if n==0:
#         print('Подвал')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком вы этаже:'))
# elevator(n1)
# def sum_list(lst):
#     if len(lst)==1:
#         return lst[0]
#     else:
#         return lst[0]+sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(251,2))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


# print(names[0])
# print(type(names[0])==list)
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][1])
# print(isinstance(names[1][1][1], list))

# def count_items(lst):
#     count=0
#     for item in lst:
#         if isinstance(item, list):
#             count+=count_items(item)
#         else:
#             count+=1
#     return count
#
#
# print(count_items(names))
#
#
# def union(s):
#     if not s:  # s==[]
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print('Выпрямленный список: ', union(names))

#
# def remove(s):
#     if not s:
#         return ''
#     if s[0] == '\t' or s[0] == ' ':
#         return remove(s[1:])
#     else:
#         return s[0] + remove(s[1:])
#
#
# print(remove('  Hel   lo\t Worl d '))


# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [1, 2, 434, 4562, 23, 52, 22]
# print(seq_search(lst, 3))
# print(seq_search(lst, 23))
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop=False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos]>item:
#                 stop=True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [1, 2, 22, 23, 52, 434, 4562]
#
#
# # print(seq_search(lst, 3))
# # print(seq_search(lst, 23))
#
#
# def binari_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midlpoint = (first + last) // 2  # 4
#         if s[midlpoint] == item:  # 13==3
#             last = midlpoint - 1
#             found = True
#         else:
#             if item < s[midlpoint]:
#                 last = midlpoint - 1
#             else:
#                 first = midlpoint + 1
#
#     return found
#
#
# print(binari_search(lst, 3))
# print(binari_search(lst, 23))

# lst1=sorted([randint(1,99) for i in range(10)])
# ch=int(input('Введите искомое число: '))
# print(lst1)
# def binari_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midlpoint = (first + last) // 2  # 4
#         if s[midlpoint] == item:  # 13==3
#             last = midlpoint - 1
#             found = True
#         else:
#             if item < s[midlpoint]:
#                 last = midlpoint - 1
#             else:
#                 first = midlpoint + 1
#     if found:
#         print('Число', item,' присутствует в списке')
#     else:
#         print('Число', item, 'отсутствует в списке')
#
#
# binari_search(lst1, ch)

#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
# #             if array[j] > array[j + 1]:
# #                 array[j], array[j + 1] = array[j + 1], array[j]
# #
# #
# #
# # a = [randint(1, 99) for i in range(10)]
# # print(a)
# # start=time.monotonic()
# # bubble(a)
# # print(a)
# # res=time.monotonic()-start
# # print(round(res,3), 'sec')
#
#
# # def sort2_func(*args):
# #     s=+args
# #     ch=int(input('Выберите тип сортировки: 1-по убыванию, 2- по возрастанию'))
# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] > r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#
#     return res
#
#
# array = [randint(1, 99) for i in range(20)]
# print(array)
# start=time.monotonic()
# array = merge_sort(array)
# print(array)
# #
# res=time.monotonic()-start
# print(round(res,3), 'sec')
# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, 'Spisok:', s)
#
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# start = time.monotonic()
# shell_sort(a)
# print(a)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# f = open('text.txt.txt', 'r')
# print(*f)
# f = open('C:\\Users\\Николай\\Desktop\\домашние задания\\DZ1 Glubokov NN\\text.txt.txt', 'r')
# print(*f)
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(f.read(3))
# print(f.read())
# f.close()
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open('Testtext.txt', 'r')
#
# c=0
# for line in f:
#     print(line)
#     c+=1
# print(c)
# f.close()
# print(f.readline())
# print(f.readline(7))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines(4))
# f = open('NewText.txt', 'w')
# print(f.write('Hello!\nWorld!'))
# f.close()
# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
# #
# f = open('text2.txt', 'r')
# rd = f.readlines()
# print(rd)
# print()
# sitr=int(input('Индекс удаляемого элемента--> '))
# for i in range(len(rd)):
#     if sitr==i:
#         del rd[i]
#     else:
#         pass
# print(rd)
# print()
# f.close()
# #
# f = open('text2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('text2.txt', 'r')
# for line in f:
#     print(line)
# print(f.read())
# f.close()


# f = open('C:\\Users\\Николай\\Desktop\\домашние задания\\DZ1 Glubokov NN\\text.txt.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f = open('C:\\Users\\Николай\\Desktop\\домашние задания\\DZ1 Glubokov NN\\text.txt.txt', 'w+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('text.txt.txt','w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt.txt','r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)


# print(get_line(lst))
# #
# with open(file_name,'w') as f:
#     f.write(get_line(lst))
#
#
#
# with open(file_name,'r') as f:
#     nums=f.read()
#     lst=nums.split(' ')
#     print(lst)
#     print(len(lst))
#
#
# print('Done!')
# file_name = 'res2.txt'
#
# with open(file_name, 'w') as f:
#     f.write(
#         'Чтобы разбить строку на фрагменты определенной длины, используйте функцию «Понимание списка» со строкой. Все фрагменты будут возвращены в виде массива. Мы также можем использовать цикл while, чтобы разделить список на части определенной длины. В этом руководстве мы узнаем, как разбить строку на фрагменты определенной длины с помощью подробных примеров программ в Python')
#
#
# def longest_text(file):
#     with open(file, 'r') as f:
#         w = f.read().split()
#         # print(w)
#         max_length = len(max(w, key=len))
#         # print(max_length)
#         res=[word for word in w if len(word)==max_length]
#         # print(res)
#         if len(res)==1:
#             return res[0]
#         return res
#
#
# print(longest_text(file_name))
#
# with open(file_name, 'r') as f:
#     lst=f.read().split()
#     print(lst)
#     max_length = max(len(word) for word in lst)
#     print([i for i in lst if len(i)==max_length])

# text='Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10'
# with open('one.txt', 'w') as f:
#     f.write(text)


# read_file='one.txt'
# write_file='two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line=line.replace('Строка', 'Линия - ')
#         fw.write(line)


import os
# print('Текущая директория: ', os.getcwd())
# print(os.listdir('.idea'))
# os.mkdir('folder')
# os.makedirs('nested1/nested2/nested3')
# os.remove('Testtext.txt')
# os.rename('nested1', 'test')
#
# os.renames('text2.txt','text/text1.txt')
# os.rmdir('folder')
# os.rmdir('text')
#
# for root, dirs, files in os.walk('test', topdown=False):
#     print('Root: ', root)
#     print('Subdirs: ',dirs)
#     print('Files: ', files)
#     print()
# for root, dirs, files in os.walk('Work'):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f'Директория {root} удалена')
import os.path


# #
# print(os.path.split(r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN'))


#
# print(os.path.dirname(r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN.py'))
# print(os.path.basename(r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN.py'))
# print(os.path.join('C:', 'Users', 'Desktop', 'Николай', 'домашние задания'))
# dirs=['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)
#
# files={
#     'Work':['w.txt'],
#     'Work/F1':['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21':['f211.txt', 'f212.txt']
# }
#
#
# for d, fl in files.items():
#     # print(d, fl)
#     for file in fl:
#         file_path=os.path.join(d, file)
#         open(file_path, 'w').close()

# file_with_text=['Work/w.txt', 'Work/F1/f12.txt','Work/F2//F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#     # for root, dirs, files in os.walk('Work', topdown=False):
#     #     print('Root: ', root)
#     #     print('Subdirs: ',dirs)
#     #     print('Files: ', files)
#     #     print()
#     # for root, dirs, files in os.walk('Work', topdown=True):
#     #     print('Root: ', root)
#     #     print('Subdirs: ',dirs)
#     #     print('Files: ', files)
#     #     print()
#
#
# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('*'*40)
#
# print_tree("Work", topdown=True)
# print_tree("Work", topdown=False)

# print(os.path.exists(r'Work/F2//F21/f211.txt'))
# print(os.path.getsize(r'Work/F2//F21/f211.txt'))
# print(os.path.getatime(r'Work/F2//F21/f211.txt'))
# print(os.path.getctime(r'Work/F2//F21/f211.txt'))
# print(os.path.getmtime(r'Work/F2//F21/f211.txt'))
#
# path = r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN\DZ for GitHub\DZ23 Glubokov NN.py'
#
# size = os.path.getsize(path)
# ksize = size // 1024
# print(ksize)
#
# c=os.path.getctime(path)
# b=time.strftime('%X.%m.%Y', time.localtime(c))
#
# # print(b)
# str2 = r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN\DZ for GitHub\DZ23 Glubokov NN.py'
#
# if os.path.exists(str2):
#     a = os.path.getctime(str2)
#     print(os.path.split(str2)[0],'\n', os.path.split(str2)[1],'\n',  a)
#
#
# else:
#     print("Not")
# #
# # print(os.path.isfile(r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN\DZ for GitHub'))
# # print(os.path.isdir(r'C:\Users\Николай\Desktop\домашние задания\DZ1 Glubokov NN\DZ for GitHub'))
# class <Name>:
#     свойство=значение
#
#     методы():#функция
#         тело метода
# class Point3D:
#     pass
# class Point:
#     '''Класс для предоставления координат точек на плоскости'''
#     x = 1
#     y = 1
#
#     def set_course(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
#
# p1.x = '100'
# p1.y = 300
# # print(type(p1))
# # print(isinstance(p1, Point3D))
# p1.set_course(3,8)
# print(p1.__dict__)
# # Point.set_course(p1, 'Elena')
# p2 = Point()
# p2.set_course(5,10)
# print(p2.__dict__)
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# print(getattr(p1, 'x'))
# print(getattr(p1, 'z', False))
# print(hasattr(p1, 'z'))
# print(hasattr(p1, 'y'))
# print(setattr(p1, 'z',7))
# print(p1.__dict__)
# print(hasattr(p1, 'z'))
#
# delattr(p1, 'z')
# print(p1.__dict__)
# p2=Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# class Human:
#     name = "name"
#     birthday="00.00.0000"
#     phone='00-00-00'
#     country='country'
#     city='city'
#     address='street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40,'*'))
#         print(f'Имя: {self.name}')
#         print(f'Дата рождения: {self.birthday}\nТелефон: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nАдрес: {self.address}\n'+'='*40)
#
#     def input_info(self, first_name,birthday, phone, country, city, address):
#         self.name=first_name
#         self.birthday=birthday
#         self.phone=phone
#         self.country=country
#         self.city=city
#         self.address=address
#     def set_name(self, name):
#         self.name=name
#
#     def get_name(self):
#         return self.name
#
#
# h1=Human()
#
# h1.print_info()
# h1.input_info('Юля',"23.05.1986","45-46-98","Россия", "Москва", "Ленина 1")
# h1.print_info()
# h1.set_name("Georg")
# h1.print_info()
# print(h1.get_name())
# class Auto:
#     name = ''
#     year = ''
#     work = ''
#     power = ''
#     color = ''
#     price = ''
#
#     def car_info(self):
#         print(
#             f'Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.work}\nМощность двигателя:'
#             f' {self.power}\nЦвет авто: {self.color}\nЦена авто: {self.price}')
#
#     def info_car(self, n, y, w, p, c, pr):
#         self.name = n
#         self.year = y
#         self.work = w
#         self.power = p
#         self.color = c
#         self.price = pr
#
#     def power_auto(self, power):
#         self.power=power
#     def super_power(self):
#         return self.power
#
# h1 = Auto()
#
# h1.info_car('BMW', "750", "Германия", "450", "Черный", "8000000")
# h1.car_info()
# h1.power_auto('400')
# print(h1.super_power())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         res = 20
#         print('Dannie sotrudnika: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f'Kvalifikacia sotrudnika {self.name}: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Constructor')
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('Inizializator')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('udalenie exemplyara ' + self.__class__.__name__)
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1
# print(p1.x)
# p2 = Point()
# print(p2.__dict__)

# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         print('Inizializator')
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
#
# p2 = Point(3, 20)
# p3 = Point()
# print(Point.count)
# print(p1.count)
# print(p2.count)

#
# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Hello! My name',self.name)
#         Robot.k += 1
#     def __del__(self):
#         print(self.name, "off")
#         Robot.k-=1
#         if Robot.k==0:
#             print(self.name, 'last')
#         else:
#             print('Working robots:', Robot.k)
#
# droid1 = Robot('R2D2')
# print(Robot.k)
# droid2 = Robot('C-3PO')
# print(Robot.k)
# droid3 = Robot('QQ-B6')
# print(Robot.k)
# droid4 = Robot('BQ-F3')
# print(Robot.k)
# del droid1
# del droid2
# del droid3
# del droid4

#
# print(Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def set_x(self, x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Coord is not int")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# # p1.set_x(100)
# # print(p1.get_x())
# # p1.set_coords(50.56, 70)
# print(p1.get_coords())
# # print(p1.__check_value)
# # print(p1.__x)
# # print(p1.__y)
# # p1.__x = 100
# # p1.y = 'abc'
# # print(p1.x)
# # print(p1.y)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x=111
# print(p1.__dict__)
#
# class Rectangle:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_perim(self):
#         return 2 * (self.__x + self.__y)
#
#     def get_gipp(self):
#         return sqrt(self.__x ** 2 + self.__y ** 2)
#
#     def print_area(self):
#         # for i in range(self.__x):
#         #     print('*'*self.__y)
#         print(('*' * self.__y + '\n') * self.__x)
#

# r1 = Rectangle(3, 4)
# a=int(input('Visota: '))
# b=int(input('Shirina: '))
# r1.set_x(a)
# r1.set_y(b)
# print(r1.get_y(), r1.get_x())
# print(r1.get_area())
# print(r1.get_perim())
# print(round(r1.get_gipp(),2))

# r1.print_area()
#
# r2 = Rectangle(2, 14)
# r2.print_area()
# r3 = Rectangle(4, 8)
# r3.print_area()

#
# class Point:
#
#     __slots__ = ['__x', '__y','z']
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def set_x(self, x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Coord is not int")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __getattr__(self, item):
#         return f'V klasse {__class__.__name__} otsutstvuet atribut "{item}"'
#
#     def __getattribute__(self, item):
#         if item == "_Point__x":
#             return 'Zakritaya peremennaya'
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == "WIDTH":
#             raise AttributeError('Nelzya izmenyati')
#         else:
#             self.__dict__[key] = value
#
#
# p1 = Point(5, 10)
# # # p1.zzz=12
# # print(p1.zzz)
# # p1.set_coords(45, 20)
# # print(p1._Point__x)
# # print(p1.get_coords())
# print(p1.__dict__)
#
# # p1.WIDTH = 4
# p1.z = 1
# print(p1.__dict__)
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__xy = y
#
#     def __set_x(self, x):
#         print('Setter')
#         if isinstance(x,(int,float)):
#             self.__x = x
#         else:
#             raise ValueError('  ***   ')
#
#     def __get_x(self):
#         print('Getter')
#         return self.__x
#
#     def __del_x(self):
#         print('Udalenie svoystva')
#         del self.__x
#
#     coordX = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5,10)
# p1.coordX=100
# print(p1.coordX)
# del p1.coordX
# print(p1.__dict__)

#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__xy = y
#
#     @property
#     def x(self):
#         print('Getter')
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print('Setter')
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError('  ***   ')
#
#
#
#     @x.deleter
#     def x(self):
#         print('Udalenie svoystva')
#         del self.__x
#
#     # coordX = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, n):
        self.__old = n

    @old.deleter
    def old(self):
        del self.__old


p1 = Person('Irina', 26)
print(p1.__dict__)
p1.name = 'Igor'
print(p1.name)
del p1.name
print(p1.__dict__)
p1.old = 'old'
print(p1.old)
del p1.old
print(p1.__dict__)