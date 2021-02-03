n = int(input())


def squares():
    number = 0
    while True:
        number += 1
        yield number, number ** 2


for i, j in squares():
    if i <= n:
        print(j)
    else:
        break
