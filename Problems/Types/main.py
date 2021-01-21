args = sys.argv

numbers = []
for arg in args[1::]:
    try:
        number = int(arg)
        numbers.append(number)
    except ValueError:
        print(f"Argument {arg} is not an int")

if len(numbers) == 4:
    print(numbers)
