max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
print(a[max], max)