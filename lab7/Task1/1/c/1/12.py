a = input()

cnt = 0
cntr = 0

for i in range(len(a)-1,-1,-1):
    cnt += 2**cntr * int(a[i])
    cntr += 1

print(cnt)