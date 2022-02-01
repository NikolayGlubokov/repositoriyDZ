from random import randint  # Задание произвольного массива
# sq=[[0 for col in range(3)] for row in range(5)]
# print(sq)
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a)
for r in a:
    for c in r:
        print(c, end='\t\t')
    print()
print()
for r in range(len(a)):
    if r%2==0:
        for row in a:
            for c in row:
                print(c, end='\t\t')
            print()
        print()
    else:
        a.sort(reverse=True)
        for row in a:
            for c in row:
                print(c, end='\t\t')
            print()
        print()