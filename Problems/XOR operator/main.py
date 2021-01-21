def xor(a, b):
    if (a and b) or (not a and not b):
        return False
    else:
        return a if a else b
