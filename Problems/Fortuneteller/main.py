number = list(input())
generator = (int(n) for n in number)
my_sum = 0

for i in generator:
    my_sum += i

print(my_sum)
