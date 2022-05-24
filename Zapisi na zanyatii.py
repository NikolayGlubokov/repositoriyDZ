# from math import *
# from random import *
# import re
# import time

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
import csv
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
#         self.__y = y
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

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, n):
#         self.__old = n
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.name = 'Igor'
# print(p1.name)
# del p1.name
# print(p1.__dict__)
# p1.old = 'old'
# print(p1.old)
# del p1.old
# print(p1.__dict__)

# class Point:
#     count = 0  # staticheskoe svoistvo
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point(5, 4)
# p2 = Point()
#
# p3 = Point()
#
# print(Point.get_count())
# print(p2.get_count())

# hfpj,hfnmcz
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# print(Change.inc(10), Change.dec(10))
#
# class Point:
#
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b > c > d:
#             return a
#         elif b > a > c > d:
#             return b
#         elif c > a > b > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b < c < d:
#             return a
#         elif b < a < c < d:
#             return b
#         elif c < a < b < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(x):
#         c=1
#         for i in range(1,x+1):
#             c*=i
#         return c
#
#
#
#
# print(Point.max(6, 7, 3, 2))
# print(Point.min(6, 7, 3, 2))
# print(Point.average(6, 7, 3, 2))
# print(Point.factorial(9))
#
# class Point:
#     count=0
#
#     @staticmethod
#     def fareng(x):
#         Point.count+=1
#         return x*(9/5)+32
#
#     @staticmethod
#     def celsius(x):
#         Point.count -= 1
#         return (x  - 32)/1.8
#
# print(Point.count)
# print(Point.fareng(15))
# print(Point.count)
# print(Point.fareng(34))
# print(Point.count)
# print(Point.celsius(93.2))
# print(Point.count)

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year} - {self.month} - {self.day}'
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_validate(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <=31 and month <= 12 and year <= 9999
#
#
# # date = Date.from_string('23.10.2021')
# # print(date.string_to_db())
# # date = Date.from_string('24.10.2021')
# # print(date.string_to_db())
#
# dates = ['30.12.2020', '20-12-2020', '01.01.2020', '12.31.2020']
#
# for string_date in dates:
#     if Date.is_date_validate(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Not")
#
# class Account:
#     suffix = 'RUB'
#     rate_eur = 0.011
#     rate_usd = 0.013
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f' Счет #{self.__num} принадлежаций {self.__surname} был открыт.')
#         print('*' * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты успешно начислены')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете: ')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'{self.__surname}')
#         self.print_balance()
#         print(f'Проценты {self.__percent:.0%}')
#         print('-' * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def withdrow_money(self,val):
#         if val<self.__value:
#             self.__value=self.__value-val
#             print(f'Вы сняли {val} {Account.suffix}')
#             self.print_balance()
#         else:
#             print(f'Снять нельзя {val} {Account.suffix}')
#             self.print_balance()
#     def add_money(self,val):
#         self.__value+=val
#         print(f'Вы внесли на счет {val} {Account.suffix}')
#         self.print_balance()
#
#     def __del__(self):
#         print('*'*20)
#         print(f'Счёт закрыт')
#
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# # print()
# # Account.set_usd_rate(2)
# # acc.convert_to_usd()
# # Account.set_eur_rate(3)
# # acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percents()
# acc.withdrow_money(200)
# acc.add_money(5000)
# acc.withdrow_money(3000)
# # acc.__del__()

#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#         #
#         # self.__fio = fio.split()
#         # self.__old = old
#         # self.__password = ps
#         # self.__weight = weight
#
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]+', fio, flags=re.IGNORECASE))
#         for s in f:
#             if s not in letters:
#                 raise TypeError('Можно использовать только буквы и дефис')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 100 лет')
#
#     @classmethod
#     def verify_weight(cls, weight):
#         if not isinstance(weight, (int, float)) or weight < 14 or weight > 1100:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 100 лет')
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат данных')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('Буквы недопустимы в серии и номере паспорта.')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#         print(self.__fio)
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self,old):
#         self.verify_old(old)
#         self.__old=old
#         print(self.__old)
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self,ps):
#         self.verify_ps(ps)
#         self.__password=ps
#         print(self.__password)
#
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self,w):
#         self.verify_weight(w)
#         self.__weight=w
#         print(self.__weight)
#
# p1 = UserDate('Глубоков Николай Николаевич', 28, '1234 567890', 105.0)
#
# print(p1.__dict__)
# p1.old=30
# p1.password='1345 999900'
# p1.weight=90
# print(p1.__dict__)
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self,*args):
#         print('Переопределенный инициализатор Line')
#         super().__init__(*args)
#         self.__width=5
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp},{self._ep},{self._color},{self._width} ')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
#
#
# class Rect(Prop):
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp},{self._ep},{self._color},{self._width} ')
#
#
# rect = Rect(Point(23, 34), Point(45, 56))
# rect.draw_line()
# print(line._width)
# print(issubclass(Line,Point))
# print(issubclass(Point, object))
# print(line.__dict__)
# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, w, h, color):
#         super().__init__(color)
#         self.__width = w
#         self.__height = h
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "red"
# print(rect.color)
# print(rect.area())
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int,float)) and isinstance(self.__y, (int,float)):
#             return True
#         return False
#     def is_int(self):
#         if isinstance(self.__x, int,) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Not')
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Not int')
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(9, 8), Point(8, 10))
# line.draw_line()

# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         self.fon = bg
#         super().__init__(w, h)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, line):
#         self.line = line
#         super().__init__(w, h)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Тип линии:', self.line)
#
# shape1 = RectFon(400, 200, 'red')
# shape1.show_rect()
# print()
# shape2=RectBorder(600,300,'1px solid black')
# shape2.show_rect()
# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str,self))
#
#
#
# v=Vector([1,2,3])
# print(v)
# print(type(v))

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int, ) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Not')
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть целочисленными")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._ep = ep
#                 self._sp = sp
#             else:
#                 print('Not int')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(9, 8), Point(8, 10))
# line.draw_line()
# line.set_coords(Point(-10,-15))
# line.draw_line()   #Дописать нормально.
#


#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int, ) and isinstance(self.__y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#
#         if sp.is_digit() and ep.is_digit():
#             self._ep = ep
#             self._sp = sp
#         else:
#             print('Not')
#
#     def draw(self):
#         raise NotImplementedError ('Not')
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
#
# figs=list()
# figs.append(Line(Point(0,0),Point(10,10)))
# figs.append(Line(Point(10,10), Point(20,10)))
# figs.append(Rect(Point(50,10), Point(20,10)))
# figs.append(Ellipse(Point(10,10), Point(20,10)))
#
#
# for f in figs:
#     f.draw()
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
# t2 = SqTable(10)
# print(t2.__dict__)
# print(t2.calc_area())
# t3 = RoundTable(radius=30)
# print(t3.__dict__)
# print(t3.calc_area())

# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             # self._width = width
#             # self._length = length
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t3 = RoundTable(radius=20)
# print(t3.__dict__)
# print(t3.calc_area())
import re
from abc import ABC, abstractmethod

# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         print('Метод move() в базовом классе')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Ферзь перемещен')
#
# q=Queen()
# q.draw()
# q.move()


# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.65
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub=self.value*Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 85.50
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub=self.value*Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d=[Dollar(5),Dollar(10),Dollar(50),Dollar(100)]
# for i in d:
#     i.print_value()
#     print(f'= {i.convert_to_rub():.2f}')
#
# d=[Euro(5),Euro(10),Euro(50),Euro(100)]
# for i in d:
#     i.print_value()
#     print(f'= {i.convert_to_rub():.2f}')

# class Father(ABC):
#
#     @abstractmethod
#     def display(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display(self):
#         print('class Child')
#
# class GrandChild(Child):
#     def display2(self):
#         print('class DisplayChild')
#
# gc=GrandChild()
# gc.display()
# gc.display2()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Метод для связи')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj=obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний класс')
# inner.inner_method()
# # print(inner.inner_name)

#
# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg=self.Lightgreen()
#
#     def show(self):
#         print("Name", self.name)
#
#     class Lightgreen:
#         def __init__(self):
#             self.name = 'Light Green'
#             self.code = 'erwer232'
#
#         def display(self):
#             print("Name:", self.name)
#             print('Code:', self.code)
#
#
# outer = Color()
# outer.show()
# q = outer.lg
# q.display()
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Employee list')
#         print(self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('ID:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('ID:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# print()
# d1.display()
# print()
# d2.display()
#
# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("class Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Class Inner')
#
#         class InnerClass:
#
#             def show(self):
#                 print('Class InnerClass')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2=inner1.inner_inner
# inner2.show()
#
# class Computer:
#     def __init__(self):
#         self.name='CP001'
#         self.os=self.OS()
#         self.cpu=self.CPU()
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#         def model(self):
#             return 'Core-i7'
#
# comp=Computer()
# my_os=comp.os
# my_cpu=comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Class Base')
#
#     class Inner:
#
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClas(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a=SubClas()
# a.display()
# # b=a.db
# b=SubClas.Inner()
# b.display1()
# b.display2()
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#     def show(self):
#         print(self.name, '==>',end=' ')
#         self.note.show()
#     class Notebook:
#         def __init__(self):
#             self.model= 'HP'
#             self.cpu= 'i7'
#             self.memory='16'
#
#         def show(self):
#             print(self.model, self.cpu, self.memory)
# s1=Student('Roman')
# s1.show()
# s2=Student("Vladimir")
# s2.show()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, 'is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name, 'is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, 'is barking')
#
#
# d = Dog('Buddy')
# d.sleep()
# d.play()
# d.bark()
#
# class A:
#     # def __init__(self):
#     #     print('Инициализатор класса А')
#     def hi(self):
#         print('A')
#
# class AA:
#     def hi(self):
#         print('AA')
#
# class B(A):
#     # def __init__(self):
#     #     print('Инициализатор класса B')
#     def hi(self):
#         print('B')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('Инициализатор класса C')
#     def hi(self):
#         print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         print('Инициализатор класса D')
#         C.__init__(self)
#     def call_hi(self):
#         C.hi(self)

#
# d = D()
# d.call_hi()
# print(D.mro())

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x},{self.__y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('нициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         Style.__init__(self, *args)
#
#
# class Line(Pos, Style):
#     def draw(self):
#         print(f'Рисование линии: {self._sp},'
#               f'{self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
# class Style:
#     def __init__(self):
#         print("Инициализатор Style")
#         # super().__init__()
#
# class Pos:
#     def __init__(self):
#         print("Инициализатор Pos")
#         # super().__init__()
#
# class Line(Pos, Style):
#     def __init__(self, color, width, sp: Point, ep: Point):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#         super().__init__()
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# l1 = Line("green", 5, Point(10, 10), Point(100, 100))
# l1.draw() Разобраться с тем, что написано выше

#
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClas(LoggerMixin, Displayer):
#     def log(self, message, filename=' '):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClas()
# subclass.display('Эта строка будет отображаться и записываться в файл')
# ghjcvjnhtnm b 'njn ghbvth
#
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Инициализатор Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.price}, {self.weight}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор Mixinlog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 ')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 3.5, 35000)
# n.print_info()
# n.save_sell_log()
# n.save_sell_log()
# print(NoteBook.mro())

#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть числом')
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#         return Clock(self.__sec - other.get_seconds())
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#         return Clock(self.__sec - other.get_seconds())
#
#     def __eq__(self, other):
#         return self.__sec == other.get_seconds()
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         return self.__sec < other.get_seconds()
#
#     def __le__(self, other):
#         return self.__sec <= other.get_seconds()
#
#     def __gt__(self, other):
#         return self.__sec > other.get_seconds()
#
#     def __ge__(self, other):
#         return self.__sec >= other.get_seconds()
#
#
# c1 = Clock(100)
# c2 = Clock(300)
# c4 = Clock(300)
# # c3=c1+c2+c4
# # c4+=c1
# #
# # print(c1.get_format_time())
# # print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# # # print(c5)
#
# if c2 == c4:
#     print('Время одинаковое')
# if c2 != c1:
#     print('Время разное')

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             # print('Neveriy index')
#             raise IndexError('Neverniy index')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             #     if 0<key<len(self.marks):
#             #         self.marks[key]=value
#             #     else:
#             #         raise TypeError('Ne v diapasone')
#             # else:
#             raise TypeError('Индекс должен быть целым положительным числом')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key,int):
#             raise TypeError('Key is not int')
#         del self.marks[key]
# s1 = Student('Mark', [5, 5, 3, 4, 5])
# print(s1.marks[2])
# print(s1[4])
# s1[2] = 4
# print(s1[2])
# print(s1.marks)
# s1[10] = 18
# print(s1.marks)
# del s1[7]
# print(s1.marks)
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть числом')
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#         return Clock(self.__sec - other.get_seconds())
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#         return Clock(self.__sec - other.get_seconds())
#
#     def __eq__(self, other):
#         return self.__sec == other.get_seconds()
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         return self.__sec < other.get_seconds()
#
#     def __le__(self, other):
#         return self.__sec <= other.get_seconds()
#
#     def __gt__(self, other):
#         return self.__sec > other.get_seconds()
#
#     def __ge__(self, other):
#         return self.__sec >= other.get_seconds()
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Key is not str')
#         if item == 'hour':
#             return (self.__sec // 3600) % 24
#         elif item == 'min':
#             return (self.__sec // 60) % 60
#         elif item == 'sec':
#             return self.__sec % 60
#
#         return 'Неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Key is not str')
#         if not isinstance(value, int):
#             raise ValueError('Value is not str')
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         if key == 'hour':
#             self.__sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.__sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.__sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
# c1['hour'] = 10
# c1['min'] = 23
# c1['sec'] = 44
# print(c1['hour'], c1['min'], c1['sec'])

#
# class Rectangle:
#     def __init__(self, w, h):
#         self.w=w
#         self.h=h
#
#     def get_perimetr(self):
#         return 2*(self.w+self.h)
#
# class Square:
#     def __init__(self,a):
#         self.a=a
#
#     def get_perimetr(self):
#         return 4*self.a
#
# class Triangle:
#     def __init__(self, a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def get_perimetr(self):
#         return self.a+self.b+self.c
#
#
#
#
# r1=Rectangle(1,2)
# r2=Rectangle(3,4)
# print(r1.get_perimetr())
# print(r2.get_perimetr())
# s1=Square(10)
# s2=Square(20)
# print(s1.get_perimetr(), s2.get_perimetr())
# t1=Triangle(1,2,3)
# t2=Triangle(4,5,6)
# print(t1.get_perimetr(),t2.get_perimetr())
#
#
# shape=[r1,r2,s1,s2,t1,t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self,value):
#         self.value=value
#
#     def total(self,a):
#         return self.value + int(a)
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self,a):
#         return len(self.value + str(a))
#
#
# t1=Number(10)
# t2=Text('Python')
# print(t1.total(35))
# print(t2.total(35))
#
# class Dog:
#     def __init__(self):
#         self.animal ='собака'
#         self.name = 'Мухтар'
#         self.age=2.5
#         self.sound='гавкает'
#
#     def info(self):
#         print(f'Я {self.animal}. Меня зовут {self.name}. Мне {self.age} лет')
#
#     def make_sound(self):
#         print(f'{self.name} {self.sound}')
#
#
# class Cat:
#     def __init__(self):
#         self.animal = 'кот'
#         self.name = 'Пушок'
#         self.age = 4
#         self.sound = 'мяукает'
#
#     def info(self):
#         print(f'Я {self.animal}. Меня зовут {self.name}. Мне {self.age} лет')
#
#     def make_sound(self):
#         print(f'{self.name} {self.sound}')
#
# d=Dog()
# c=Cat()
#
# for g in d,c:
#     g.info()
#     g.make_sound()

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def info(self):
#         return f'{self.first, self.last, self.age}'
#
#
# class Student(Human):
#     def __init__(self, spec, group, rang, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.group = group
#         self.rang = rang
#
#     def info(self):
#         return f'{self.spec, self.group, self.rang}'
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, exp, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#
#         return f'{self.spec, self.exp}'
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, spec, exp, first, last, age):
#         super().__init__(spec, exp, first, last, age)
#         self.topic = topic
#
#     def info(self):
#
#         return f'{self.topic}'
#         super().info()
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     # Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     print(i.info())

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#     def info(self):
#         print(f"{self.first} {self.last} {self.age}")
# class Student(Human):
#     def __init__(self, spec, group, reit, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.group = group
#         self.reit = reit
#     def info(self):
#         print(f"{self.spec} {self.group} {self.reit}", end=" ")
#         super().info()
#
# class Teacher(Human):
#     def __init__(self, spec, exp, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.exp = exp
#     def info(self):
#         print(f"{self.spec} {self.exp}", end=" ")
#         super().info()
#
# class Graduate(Student):
#     def __init__(self, topic, first, last, age, spec, group, reit):
#         super().__init__(first, last, age, spec, group, reit)
#         self.topic = topic
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
# group = [
# Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
# Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
# Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
# Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
# Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
# Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()
#
# class Cat:
#     def __init__(self,name):
#
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}:{self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
# cat = Cat('Пушок')
# print(cat)
#
# class Point:
#     def __init__(self,*args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
# p=Point(1,2,3)
# print(len(p))

# class Point:
#     __slots__ = ('x','y', '__length')
#
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.length=sqrt(x**2+y**2)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length=value
#
#
# p1 = Point(2,8)
# print(p1.length)
# p1.__slots__.z=22
# # print(p1.__dict__)

# class Point:
#     '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Point2D:
#     __slots__ = ('x', 'y',)  #
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# pt=Point(1,2)
# pt2=Point2D(1,2)
#
# print('pt=', pt.__sizeof__())
# print('pt2=', pt2.__sizeof__()+pt2.__dict__.__sizeof__())

# class Point3D(Point2D):
#     __slots__ = 'z'
#
#     def __init__(self, x,y,z):
#         super().__init__(self,x,y)
#         self.z = z
#
#
#
# pt2=Point2D(1,2)
# pt3=Point3D(2,3,4)
#
#
# print(pt3.__dict__

# class Counter:
#     def __init__(self):
#         self.count=0
#     def __call__(self, *args, **kwargs):
#         self.count+=1
#         print(self.count)
#
#
# c1=Counter()
# c1()
# c1()
# c2=Counter()
# c2()
#
# class StripChars:
#     def __init__(self, chars):
#         self.chars=chars
#
#     def __call__(self, a):
#         if not isinstance(a,str):
#             raise ValueError('Avalaible type')
#         return a.strip(self.chars)
#
# s1=StripChars(' &?!@#$%##')
# print(s1(' @Hello World! '))
#
# def strio_chars(chars):
#     def wrap(string):
#         if not isinstance(string,str):
#             raise ValueError('Avalaible type')
#         return string.strip(chars)
#
#
#     return wrap
#
#
#
#
# s1=strio_chars(' &?!@#$%##')
#
# print(s1(' @Hello World! '))
#
# class SortSurname:
#     def __init__(self, surname, name, age):
#         self.surname=surname
#         self.name=name
#         self.age=age
#
#
#     @property
#     def data(self):
#         return self.surname,self.name,self.age
#
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#
#     def __call__(self, lst):
#         lst.sort(key= lambda i: [i.__dict__[key] for key in self.__method])
#
# p=[SortSurname('Иванов', 'Игорь', 28),
#    SortSurname('Петров', 'Степан', 21),
#    SortSurname('Сидоров', 'Антон', 25),
#    SortSurname('Петров', 'Анатолий', 11),
#    SortSurname('Иванов', 'Иван', 28)]
#
# for i in p:
#     print(i.data)
#
# s1=SortKey('surname', 'name')
# s1(p)
# print()
# for i in p:
#     print(i.data)
#
# print()
#
# s2=SortKey('surname', 'age')
# s2(p)
#
# for i in p:
#     print(i.data)
#
# class MyDecorator:
#     def __init__(self, func):
#         self.func=func
#
#     def __call__(self):
#         print('Перед вызовом')
#         self.func()
#         print('После вызова')
#
# @MyDecorator
# def func1():
#     print('func')
#
# func1()

#
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         print(res)
#         return res**2
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 5))

#
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         res = self.func(*args,**kwargs)
#         print(res)
#         return res**2

#
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             print('*' * 10)
#             res=func(*args, **kwargs)
#
#             print(res**self.name)
#             print('*' * 10)
#
#         return wrap
#
#
# @MyDecorator(4)
# def add(a, b):
#    print(a*b)
#    return a*b
#
# add(2,5)

#
# def dec(fn):
#     def wrap(*args,**kwargs):
#         print('*'*10)
#         fn(*args,**kwargs)
#         print('*' * 10)
#     return wrap
#
#
#
#
# class Person:
#
#     def __init__(self, name, surname):
#         self.name=name
#         self.surname=surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
#
# p1=Person('Виталий', 'Карасев')
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value*2
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Инициализатор ActualClass')
#
#     def quad(self, value):
#         return value*4
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(5))

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name=value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @name.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person('Ivan', 'Petrov')
# print(p.name.get())
#


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.name=name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.name} must be str')
#         instance.__dict__[self.name] = value
#
#
# class Person:
#
#     name = ValidString()
#     surname=ValidString()
#     def __init__(self, name, surname):
#         self.name =name
#         self.surname = surname
#
# p = Person('Ivan', 'Petrov')
# print(p.name)
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'{self.name} must be str')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price=ValidString()
#     value=ValidString()
#     def __init__(self, name, value, price):
#         self.name = name
#         self.value = value
#         self.price = price
#
#     def total(self):
#         return self.price * self.value
#
#
# p = Order('apple', 5, 10)
# print(p.total())
#
# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError('Nea')
#
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name]=value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# a=5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_lenght(self):
#         return len(self)


# MyList=type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst=MyList()
# lst.append(10)
# lst.append(20)
# print(lst, lst.get_length())
#
# class MyMetaClass(type):
#     def __new__(mcs, name, base, attr):
#         print('Sozdanie novogo objecta', name)
#         return super(MyMetaClass, mcs).__new__(mcs, name, base, attr)
#
#     def __init__(cls, name, base, attr):
#         print('Inicializator classa', name)
#         super(MyMetaClass,cls).__init__(name, base, attr)
#
#
# class Student(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud=Student('Anna')
# print('Bvz studenta:', stud.get_name())

# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian
#
# # from geometry import *
#
# # r1 = geometry.rect.Rectangle(1, 2)
# # r2 = geometry.rect.Rectangle(3, 4)
# # s1 = geometry.sq.Square(10)
# # s2 = geometry.sq.Square(20)
# # t1 = geometry.trian.Triangle(1, 2, 3)
# # t2 = geometry.trian.Triangle(4, 5, 6)
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
# s1 = sq.Square(10)
# s2 = sq.Square(20)
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())

# from car import electrocar
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
# if __name__=='__main__':
#     main()

# dump() - сохраняет данные в файл
# dumps() - в оперативную память
# load() - десерилизация (считывание) данных из файла
# loads() - из памяти
import pickle

#
# filename = 'basket.txt'
#
# shop_list= {
#     'fruit':['apples', 'mango'],
#     'vegetables':['carrot'],
#     'budget':1000
# }
#
# with open(filename,'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename,'rb') as fh:
#     shop_list_2=pickle.load(fh)
#
# print(shop_list_2)

# class Text:
#     a_number = 35
#     a_string='Hello'
#     a_list=[1,2,3,4,5]
#     a_dict={'first':'a', 'second':2, 'third':[1,2,3]}
#     a_tuple=(22,33)
#
#     def __str__(self):
#         return f'Число: {Text.a_number}\n'\
#                f'Число: {Text.a_string}\n'\
#                f'Число: {Text.a_list}\n'\
#                f'Число: {Text.a_dict}\n'\
#                f'Число: {Text.a_tuple}\n'
# obj=Text()
#
# my_obj=pickle.dumps(obj)
# print(my_obj)
#
# l_obj=pickle.loads(my_obj)
# print(l_obj)
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'sdfsdf'
#         self.c = lambda x: x ** 2
#
#     def __str__(self):
#         return f'{self.a}, {self.b}, {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x ** 2
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
#
# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
# 
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
# 
#         return f'{self.count}:{line}'
# 
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         self.file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
# 
#         self.file = file
# 
# 
# reader = TextReader('dream.txt')
# print(reader.read_line())
# print(reader.read_line())
# 
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())


# #JSON


import json

# data = {
#   'firstName': 'Jane',
#   "lastName": "Doe",
#   "hobbies": ("running", "sky diving", "singing"),
#   "age": 35,
#   "children": [
#     {
#       "firstName": "Alice",
#       "age": 6
#     },
#     {
#       "firstName": "Bob",
#       "age": 8
#     }
#   ]
# }

# with open("data_file.json", 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", 'r') as fw:
#     data1 = json.load(fw)
#     print(data1)

# json_string = json.dumps(data, sort_keys=True)
#
# data1 = json.loads(json_string)
# print(data1)

# x = {'name': 'Виктор'}
# y = {'name': 'Виктор'}
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(personal_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(personal_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         c = ''
#         for i in self.marks:
#             c += str(i) + ', '
#         # s = str(self.marks).replace('[', '')
#         # s1 = s.replace(']', '')
#         # return f"Студент {self.name}: {s1}"
#         return f'Student: {self.name}: {c[:-2]}'
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         c = ''
#         for i in self.students:
#             c += str(i) + '\n'
#         return f"Группа: {self.group}\n{c}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_lst = []
#             for i in group.students:
#                 stud_lst.append([i.name, i.marks])
#             tmp = {"Students": stud_lst}
#             data.append(tmp["Students"])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 5)
# # print(st1)
# # print(st1.average_mark())
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# print(my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
#
# # Student.dump_to_json(st1, 'student.json')
# # Student.dump_to_json(st2, 'student.json')
# # Student.dump_to_json(st3, 'student.json')
# #
# # Student.load_from_file('student.json')
#
# Group.dump_group('group.json', my_group2)
# Group.dump_group('group.json', my_group)
# Group.upload_group("group.json")

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # print(todos[:10])
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_completed = top_users[0][1]
# print(max_completed)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_completed:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = " and ".join(users)
#
# s = 's' if len(users) > 1 else ''
# print(f"user{s} {max_users} completed {max_completed} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as data_file:
#     filter_todos = list(filter(keep, todos))
#
#     json.dump(filter_todos, data_file, indent=2)
#
# with open("filtered_data_file.json", 'r') as fw:
#     data = json.load(fw)
#     print(data)
# Имя;Профессия;Год рождения
# Виктор;Вэб-дизайнер;1995
# Игорь;Программист;1983

# CSV (Comma Separated Values)
import csv
#
# with open('database.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=",")
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")
#
#
# with open('database.csv') as r_file:
#     fieldnames = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=",", fieldnames=fieldnames)
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open('student.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data_new.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open('sw_data_new.csv') as f:
#     print(f.read())


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data_new1.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(data)
#
# with open('sw_data_new1.csv') as f:
#     print(f.read())

# with open("student1.csv", 'w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': 'Саша', 'Возраст': '6'})
#     file_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
#     file_writer.writerow({'Имя': 'Вова', 'Возраст': '14'})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     write = csv.DictWriter(f, fieldnames=list(data[0].keys()), lineterminator="\r")
#     write.writeheader()
#     for d in data:
#         write.writerow(d)

# from bs4 import BeautifulSoup
#

# def get_salary(s):
#     pattern=r'\d+'
#     res=re.findall(pattern,s)[0]
#     print(res)
# # def get_copywriter(tag):
# #     whois=tag.find('div', class_='whois')
# #     if 'Copywriter' in whois:
# #         return tag
# #     return None


# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[1].find('div', class_='links')
# # row = soup.find_all("div", {"data-set": "salary"})
# # row = soup.find_all("div", text='Alena')
# # row = soup.find("div", text='Alena').parent
# # row = soup.find("div", text='Alena').find_parent(class_='row')
# # row=soup.find('div', id='whois3').find_next_sibling()
# # row=soup.find('div', id='whois3').find_previous_sibling()
# print(row)
# copywriter=[]
# row = soup.find_all('div', class_='row')
# print(row)
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# salary=soup.find_all('div', {'data-set':'salary'})
# # print(salary)
# for i in salary:
#     get_salary(i.text)
import requests
from bs4 import BeautifulSoup


#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     res=re.sub(r'\D+','',s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer=csv.writer(f, lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     # p1=soup.find('header', id='masthead').find('p', class_='site-title').text
#     s = soup.find_all('section', class_='plugin-section')[1]
#     plugins = s.find_all('article')
#     # return len(plugins)
#     for plugin in plugins:
#         name=plugin.find('h3').text
#         url=plugin.find('h3').find('a').get('href')
#         rating=plugin.find('span', class_='rating-count').find('a').text
#         r=refined(rating)
#
#         data = {'name':name, 'url':url, 'rating':rating}
#         print(data)
#         write_csv(data)
#
# def main():
#     urs = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(urs))
#
#
# # r = requests.get('https://ru.wordpress.org/')
# # print(r.status_code)
# # print(r.headers['Content-Type'])
# # r.encoding='utf-8'
# # print(r.text)
# if __name__ == '__main__':
#     main()

#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     for i in range(1,4):
#         urs = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_page_data(get_html(urs))
#
#
# def refined_cy(s):
#     return s.split()[-1]
#
# def write_csv(data):
#     with open('plugins2.csv', 'a') as f:
#         writer=csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all('article', class_='plugin-card')
#     print(elements)
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refined_cy(c)
#         except ValueError:
#             c = ''
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
# if __name__ == '__main__':
#     main()
#
# from parser import Parser
#
# def main():
#     pars=Parser('https://www.ixbt.com/live/index/type/news/','news.txt')
#     pars.run()
# if __name__=='__main__':
#     main()
#Sozdanie svoey programmi articles
