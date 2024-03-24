n = int(input())
cnt = 2

while cnt <= n:
    if n%cnt==0:
        print(cnt)
        break
    cnt+=1