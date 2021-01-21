code = int(input())

result = chr(code) if 32 <= code <= 126 else False
print(result)
