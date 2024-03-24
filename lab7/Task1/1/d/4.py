a = input().split()

for i in range(len(a)):
    if i!=len(a)-1 and a[i] > a[i+1]:
        print(a[i])
