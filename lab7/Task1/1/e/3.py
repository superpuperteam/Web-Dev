def xor(x, y):
    return (x or y) and not (x and y)
    
a = bool(input())
b = bool(input())

print(xor(a, b))