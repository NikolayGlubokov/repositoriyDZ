

def check_password(n, even=True):
    sum = 0
    while n > 0:
        cur_digit = n % 10
        if even and cur_digit % 2 == 0:
            sum += cur_digit
        if not even and cur_digit % 2 != 0:
            sum += cur_digit
        n //= 10

    return sum


print(check_password(754622, even=False))


def display_info(name, age):
    print('Name:', name, "\n Age:", age, "\n")


display_info('Ira', 23)
display_info(age=23, name='Ira')
display_info('Igor', 23)


def func(a, ln=None):
    if ln is None:
        ln = []
    ln.append(a)
    return ln


print(func(1))
print(func(1))
print(func(1))
a = 5
b = 5
print(id(a))
print(id(b))

lt = [1, 2, 3, 4]
lt1 = [1, 2, 3, 4]
print(id(lt))
print(id(lt1))
print(lt == lt1)
print(lt is lt1)


def add_number(n):
    print('Vnutri funkcii: ', n, '=', id(n))
    n += 1
    print('Posle prisvoeniya:', n, '=', id(n))
    return n


x = 1
print(x, '=', id(x))
a = add_number(x)
print(a, '=', id(a))

cp=tuple([2**i for i in range(12)])
print(cp)
def slicer(x, y):
    lst = []
    for i in range(len(x)):
        if x[i] == y:
            lst.append(i)
    x1 = x[lst[0]:lst[1] + 1]
    return x1

print(slicer(sd, -1))