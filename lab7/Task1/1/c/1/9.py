a = int(input())

cnt = 0

for i in range(a+1):
    if i!=0 and a%i==0:
        cnt+=1

print(cnt)