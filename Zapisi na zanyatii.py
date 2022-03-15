from math import *
from random import *
import re

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

s='int=4,float=4.0, double=8.0f'
#reg=r'\w+\s*=\s*\d[.\w+]*'
# #reg=r'(int|float)\s*=\s*\d[.\w+]*'
# reg=r'((int|float)\s*=\s*\d[.\w+]*)'
print(re.findall(reg,s))
