def min( a, b, c, d):
    mas = [a,b,c,d]
    mas.sort()
    return mas[0]

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a,b,c,d))