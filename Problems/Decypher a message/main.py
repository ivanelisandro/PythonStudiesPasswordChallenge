encoded = bytes(input(), 'utf-8')
raw_key = int(input())

bytes_key = raw_key.to_bytes(2, 'little')
key = bytes_key[0] + bytes_key[1]

decoded = [b + key for b in encoded]

print(str(bytes(decoded), 'utf-8'))
