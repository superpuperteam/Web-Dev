n = int(input())
cnt = 0

while cnt <= n:
    if 2**cnt == n:
        print("YES")
        break
    if cnt==n:
        print("NO")
    cnt+=1