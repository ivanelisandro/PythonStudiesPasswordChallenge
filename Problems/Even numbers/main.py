n = int(input())


def even():
    number = 0
    iteration = 1
    while True:
        yield iteration, number
        iteration += 1
        number += 2


for i, j in even():
    if i <= n:
        print(j)
    else:
        break
